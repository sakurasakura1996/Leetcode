""""
417. 太平洋大西洋水流问题
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。
规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。
提示：
输出坐标的顺序不重要
m 和 n 都小于150
示例：
给定下面的 5x5 矩阵:
  太平洋 ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋
返回:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
"""
from functools import lru_cache
from typing import List
# class Solution:
#     def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # 下面的代码写了半天还是搞不定，我们应该从边界开始逆向追溯，从大西洋边界能够追溯到的就是能够到达大西洋的，从太平洋边界能够遍历到的就是
        # 能到达太平洋的。
        # if not matrix:
        #     return []
        # m = len(matrix)
        # n = len(matrix[0])
        # direction = [[-1, 0],[0, 1],[1, 0],[0, -1]]
        # visited = [[0] * n for _ in range(m)]
        # @lru_cache(None)
        # def dfs(x,y):
        #
        #     visited[x][y] = 1
        #     ret = [False, False]
        #     if x == 0 or y == 0:
        #         ret[0] = True
        #     if x == m-1 or y == n-1:
        #         ret[1] = True
        #     for i in range(4):
        #         new_x = x + direction[i][0]
        #         new_y = y + direction[i][1]
        #         if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and matrix[new_x][new_y] <= matrix[x][y]:
        #             tmp = dfs(new_x, new_y)
        #             ret = ret or tmp
        #         elif 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and matrix[new_x][new_y] <= matrix[x][y]:
        #             ret = ret or dfs(new_x,new_y)
        #     return ret
        #
        # ans = []
        # for i in range(m):
        #     for j in range(n):
        #
        #         cur = dfs(i,j)
        #         if cur == [True, True]:
        #             ans.append([i, j])
        # return ans


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        # 流向太平洋的位置
        res1 = set()
        # 流向大西洋的位置
        res2 = set()
        row = len(matrix)
        col = len(matrix[0])

        def dfs(i, j, res):
            res.add((i,j))
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and matrix[i][j] <= matrix[tmp_i][tmp_j] and (tmp_i, tmp_j) not in res:
                    dfs(tmp_i, tmp_j, res)

        for i in range(row):
            dfs(i, 0, res1)
        for j in range(col):
            dfs(0, j, res1)
        for i in range(row):
            dfs(i, col - 1, res2)
        # 大西洋
        for j in range(col):
            dfs(row - 1, j, res2)

        return list(res1 & res2)


solu = Solution()
matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
ans = solu.pacificAtlantic(matrix)
print(ans)

