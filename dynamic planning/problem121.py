"""
121.买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
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
# 自己写的动态规划，虽然对了但是不好，我这里的dp[i]表示的是，第i天卖掉股票的最大利润，
# 因为获得最大利润的话总有一天是要被卖出去的，如果第i天的价格大于前一天的价格，那么肯定今天卖出去
# 如果没有前一天价格高呢，但是还是要今天卖，那就有可能是负数了，那就和0比较下最大值
# from typing import List
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) == 0 or len(prices) == 1:
#             return 0
#         dp = [0 for i in range(len(prices))]
#         dp[1] = max(0, prices[1]-prices[0])
#         for i in range(2,len(prices)):
#             if prices[i] > prices[i-1]:
#                 dp[i] = dp[i-1]+prices[i]-prices[i-1]
#             else:
#                 dp[i] = max(0,dp[i-1]+prices[i]-prices[i-1])
#         return max(dp)

# way1 另一种写法，更好一些。
# 这个动态规划的方法更加适合一些。dp[i]表示前i天的最大利润。  那么
# dp[i] = max(dp[i-1], prices[i]-minprice)
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0 # 边界条件
        dp = [0] * n
        minprice = prices[0]

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]


# way2 遍历一遍数组，计算每次 到当天为止 的最小股票价格和最大利润。
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


solu = Solution()
prices = [2,1,2,1,0,1,2]
ans = solu.maxProfit(prices)
print(ans)

