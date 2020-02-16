"""
不同路径二
1.还是定义好数组，搞清楚数组元素的值代表的含义
2.数组元素之间的关系
3.初始值
yes,终于自己独立的搞出了一题
"""

from typing import List
import numpy as np
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ans = list(np.ones((m, n)).astype(int))
        # 第一行和第一列的情况下，机器人只能往右走或者往下走，而且还要看看路上是否有路障
        for i in range(0,m):
            if obstacleGrid[i][0] == 1:
                for j in range(i,m):
                    ans[j][0] = 0
        for i in range(0,n):
            if obstacleGrid[0][i] == 1:
                for j in range(i,n):
                    ans[0][j] = 0
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    ans[i][j] = 0
                else:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1]
        return ans[m-1][n-1]

a = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
solu = Solution()
ans = solu.uniquePathsWithObstacles(a)
print(ans)





