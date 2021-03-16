from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 可以在纸上找到规律
        n = len(matrix)
        if n%2:
            # 如果n为奇数的话
            for i in range(n//2 + 1):
                for j in range(n//2):
                    matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i] = \
                    matrix[n - j - 1][i], matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1]
        else:
            for i in range(n//2):
                for j in range(n//2):
                    matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] = matrix[n-j-1][i], \
                    matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1]
        print(matrix)


if __name__ == '__main__':
    solu = Solution()
    matrix = [[1]]
    solu.rotate(matrix)
