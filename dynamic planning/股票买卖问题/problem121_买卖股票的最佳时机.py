"""
121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int])->int:
        # 这道题属于股票交易系列中最简单的题目，属于动态规划系列中的，但是这道题简单题，
        # 可以不用动态规划，不过最好我们也要思考其中蕴含的动态规划思想
        # 下面的解法就是比较简单的动态规划思想。
        if not prices or len(prices) == 1:
            return 0
        dp = [0 for _ in range(len(prices))]
        # dp[1] = max(0, prices[1] - prices[0])
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                dp[i] = dp[i-1] + prices[i] - prices[i-1]
            else:
                dp[i] = max(0, dp[i-1]+prices[i]-prices[i-1])
        return max(dp)

    def maxProfit_2(self, prices: List[int]) -> int:
        # 尝试使用滑动窗口方法来解决问题
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)
        left = 0
        right = 1
        ans = 0
        while right < n:
            if prices[right] > prices[left]:
                ans = max(ans, prices[right] - prices[left])
            while prices[right] < prices[left]:
                left += 1
            right += 1
        return ans

solu = Solution()
prices = [7,1,5,3,6,4]
ans = solu.maxProfit_2(prices)
print(ans)

