"""
188. 买卖股票的最佳时机 IV
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1：
输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

示例 2：
输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
提示：
0 <= k <= 109
0 <= prices.length <= 104
0 <= prices[i] <= 1000
"""
# 这道题是上一道题的抽象版，上一道题是最多只能完成2笔交易，这里是最多k笔交易不固定了。其实思路还是一样的啊
# 动态规划多一个状态而已，不过还是要求对动态规划的思路足够清晰才行。
# 我想再强调一下这里的dp数组中k的含义，就是代表前i天，最多可以交易j次的含义。所以后面代码中我们才能看到
# dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i]) 今天持有了股票，可能是前天就已经有了
# 也有可能是今天买的，那就是昨天之前持空，但是最多只能交易j-1次，因为今天要交易一次啊。理解了就行。
from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]):
        n = len(prices)
        if not prices or n == 1 or k == 0:
            return 0

        if k > n//2:
            # k > n//2时，我们可以简化为无限次交易了，因为交易次数肯定用不完，所以就是无限次了啊。
            # 这样可以省下时间。
            dp = [[0] * 2 for _ in range(n)]
            # 边界初始化
            # dp[0][0] = 0
            dp[0][1] = -prices[0]
            for i in range(1, n):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

            return dp[n - 1][0]

        dp = [[[0, 0] for _ in range(k+1)] for i in range(n)]
        # dp[0][k-1][1] = -prices[0]
        for i in range(k+1):
            dp[0][i][1] = - prices[0]
        for i in range(1, n):
            dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1] + prices[i])
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][0] - prices[i])
        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        # print(dp)
        return dp[n-1][k-1][0]


solu = Solution()
k = 2
prices = [2,4,1]
ans = solu.maxProfit(k, prices)
print(ans)