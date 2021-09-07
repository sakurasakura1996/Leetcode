from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 原地修改数组, 首先说明，下面代码是自己一上来就犯的错误，我们如果遇到一个0就把行列都改了，等下访问到后面，
        # 原来已经不是0的结果值被改动了。所以直接遍历修改数值肯定不对啊，怪不得题目说空间复杂度要求为常数级
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i] = [0] * n
                    for k in range(m):
                        matrix[k][j] = 0
        print(matrix)

    def setZeroes2(self, matrix: List[List[int]]) -> None:
        # 我们先使用 O(mn)空间复杂度的方法，最容易想到
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    ans.append([i,j])
        for x, y in ans:
            for i in range(m):
                matrix[i][y] = 0
            for j in range(n):
                matrix[x][j] = 0
        print(matrix)

    def setZeroes3(self, matrix: List[List[int]]) -> None:
        # 空间复杂度为 O(m+n)的方法，用两个数组记录行和列中有0的元素
        m = len(matrix)
        n = len(matrix[0])
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        print(matrix)

    def setZeroes4(self, matrix: List[List[int]]) -> None:
        # 空间复杂度为常数的方法： 使用两个标记变量
        #　我们可以用矩阵的第一行 和第一列来代替方法一中两个标记数组，以达到 O(1)的额外空间。但这样会导致原数组的第一行和第一列被修改。
        # 因此，我们需要额外使用两个标记变量分别记录第一行和第一列是否原本包含0
        m = len(matrix)
        n = len(matrix[0])
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0
        if flag_row0:
            for i in range(n):
                matrix[0][i] = 0
        print(matrix)


if __name__ == '__main__':
    solu = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solu.setZeroes4(matrix)
