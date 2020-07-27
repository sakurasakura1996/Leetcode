"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""
#这道题应该是用动态规划做就行了吧。
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return None
        row = len(grid)
        col = len(grid[0])
        # dp[i][j]表示从左上角走到（i,j）时路径上的数字总和为最小
        # 边界初始化
        for i in range(1, col):
            grid[0][i] += grid[0][i-1]
        for i in range(1, row):
            grid[i][0] += grid[i-1][0]
        for i in range(1,row):
            for j in range(1,col):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[row-1][col-1]

solu = Solution()
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
ans = solu.minPathSum(grid)
print(ans)
