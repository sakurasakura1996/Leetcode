"""
最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
这类动态规划的题目，在识别出它可以用动态规划方法求解，那我们就要根据动态规划的方法步骤来做，思路就会清晰很多
1.定义数组元素的含义
2.找出关系数组元素间的关系式
3.找出初始值
我们根据这种步骤一步一步来写，简单的动态规划并不是特别难了
"""

from typing import List
import numpy as np
class Solution:
    def minPathSum(self,grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m <= 0 or n <= 0:
            return 0
        ans = list(np.zeros((m,n)).astype(int))
        ans[0][0] = grid[0][0]
        for i in range(1, m):
            ans[i][0] = ans[i-1][0] + grid[i][0]
        for i in range(1, n):
            ans[0][i] = ans[0][i-1] + grid[0][i]
        for i in range(1,m):
            for j in range(1, n):
                ans[i][j] = min(ans[i-1][j],ans[i][j-1])+grid[i][j]
        return ans[m-1][n-1]

a = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
solu = Solution()
ans = solu.minPathSum(a)
print(ans)