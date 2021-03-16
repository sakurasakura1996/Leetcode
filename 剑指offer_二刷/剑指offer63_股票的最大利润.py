"""
剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
限制：
0 <= 数组长度 <= 10^5
注意：本题与主站 121 题相同
"""
# 这道题属于股票交易的简单题，我们不一定非要用动态规划来写，但是一定要得会写
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:return 0
        n = len(prices)
        dp = [0] * (n)
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i-1], prices[i]-min_price)

        return max(dp)


if __name__ == '__main__':
    solu = Solution()
    prices = [7,6,5,4,1]
    ans = solu.maxProfit(prices)
    print(ans)