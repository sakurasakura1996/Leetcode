from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """这个问题相比上一个问题，交易次数由一次变为尽可能多次，只要能交易就不限制次数"""
        n = len(prices)
        if n == 1:
            return 0
        # 这道题用动态规划来解决吧，因为没有交易次数的限制，所以我们并不需要定义交易次数的状态，只需要定义天数和交易状态（买入，卖出，不动）
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = - prices[0]  # 买入
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        # print(dp)
        return dp[n-1][0]


if __name__ == '__main__':
    solu = Solution()
    prices = [7,1,5,3,6,4]
    ans = solu.maxProfit(prices)
    print(ans)
