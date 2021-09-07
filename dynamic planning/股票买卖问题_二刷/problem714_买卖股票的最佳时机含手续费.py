from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 我们可以将支付手续费算在买入股票或者卖出股票的时候
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        dp = [[0, 0] for _ in range(n)]

        # 设置 买入股票的时候交手续费
        dp[0][1] = -prices[0]
        dp[0][0] = 0

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]


if __name__ == '__main__':
    solu = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    ans = solu.maxProfit(prices, fee)
    print(ans)