"""
面试题 17.09. 第 k 个数
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。
例如，前几个数按顺序应该是 1，3，5，7，9，15，21。
示例 1:
输入: k = 5
输出: 9
"""
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        p3 = 0
        p5 = 0
        p7 = 0
        dp = [1] * k
        for i in range(1, k):
            ans = min(dp[p3] * 3, dp[p5] * 5, dp[p7] * 7)
            if dp[p3] * 3 == ans:
                p3 += 1
            if dp[p5] * 5 == ans:
                p5 += 1
            if dp[p7] * 7 == ans:
                p7 += 1
            dp[i] = ans
        return dp[k-1]