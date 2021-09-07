from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """该问题要求是：股票只能买卖一次所能获得的最大利润"""
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)
        dp = [0] * n
        ans = 0
        # dp[i]表示第i天卖掉股票所得的收益
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                dp[i] = dp[i-1] + prices[i] - prices[i-1]
            else:
                dp[i] = max(0, dp[i-1] + prices[i] - prices[i-1])
            ans = max(ans, dp[i])
        return ans

    def maxProfit2(self, prices: List[int]) -> int:
        # 我们尝试使用滑动窗口方法来解决问题
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)
        left, right = 0, 1
        ans = 0
        while right < n:
            if prices[right] > prices[left]:
                ans = max(ans, prices[right] - prices[left])
            while prices[right] < prices[left]:
                left += 1
            right += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    prices = [7,1,5,3,6,4]
    ans = solu.maxProfit2(prices)
    print(ans)