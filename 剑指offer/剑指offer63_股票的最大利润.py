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
# 这个系列，当时都做过，现在再做好像又不是很清晰了。应该是可以用动态规划来解决的，那么用到动态规划，我们就要去联想
# 动态规划怎么解题，首先，思考下这个问题到底有几个变化的状态，然后定义出dp数组，初始化边界情况，然后再找到递推关系。
# 分析这个问题，我觉得有两个状态，第一个是某一天，第二个是当前是买入了还是卖出了还是一直没有入手。
# 分析到这，编码的时候我突然不知道该怎么限制只允许交易一次的问题了。
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n == 0 or n == 1:return 0
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], - prices[i])  # 因为只允许交易一次，所以这次买入的话，那么说明之前一直没买过。
        return dp[n-1][0]

    def maxProfit2(self, prices: List[int]) ->int:
        # 滑动窗口方法来看看能不能写出来
        n = len(prices)
        if n == 0 or n == 1:return 0
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


if __name__ == '__main__':
    solu = Solution()
    prices = [7,1,5,3,6,4]
    ans = solu.maxProfit(prices)
    print(ans)


