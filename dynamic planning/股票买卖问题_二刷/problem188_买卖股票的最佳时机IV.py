from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)
        dp = [[[0, 0] for _ in range(k+1)] for _ in range(n)]

        # 初始化才是关键问题
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')

        for j in range(1, k+1):
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[n-1][k][0]


if __name__ == '__main__':
    solu = Solution()
    k = 2
    prices = [3,2,6,5,0,3]
    ans = solu.maxProfit(k, prices)
    print(ans)

