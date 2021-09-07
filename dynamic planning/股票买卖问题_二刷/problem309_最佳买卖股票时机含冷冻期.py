from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """这道题的要求是交易之后（卖出）无法第二天就买入股票，那么我是否可以将冷冻期那天单独设置一个状态呢"""

        if not prices or len(prices) == 1:
            return 0

        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        # 初始化
        dp[0][1] = - prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])

        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[n-1][0]


if __name__ == '__main__':
    solu = Solution()
    prices = [1,2,3,0,2]
    ans = solu.maxProfit(prices)
    print(ans)