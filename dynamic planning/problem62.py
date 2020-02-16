"""
不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 0 or n <= 0:
            return 0
        ans = list(np.zeros((m, n)).astype(int))     # 先创建一个二维数组
        # 动态规划有三步，第一步，定义数组元素的含义，直接定义好每个元素所代表的含义
        # 第二步定义初值，第三步定义元素间的关系

        for i in range(m):
            ans[i][0] = 1
        for i in range(n):
            ans[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = ans[i-1][j]+ans[i][j-1]
        return ans[m-1][n-1]


solu = Solution()
ans = solu.uniquePaths(3,2)
print(ans)
