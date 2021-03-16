"""
剑指 Offer 14- I. 剪绳子
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，
此时得到的最大乘积是18。
示例 1：
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：
2 <= n <= 58
注意：本题与主站 343 题相同
"""
# 首先想到的念头：是不是用动态规划来写啊
# 下面的写法是自己找规律找出来的，因为n>=8时，我们可以通过动态规划来写，但是
# 前面的部分还是不能用，但是前面部分的解答都是 两数相乘取最大值，
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1] * 59
        dp[0] = 0
        dp[1] = 0
        for i in range(2, 8):
            if i % 2 == 1:
                dp[i] = (i//2) * (i-i//2)
            else:
                dp[i] = (i//2) * (i//2)
        if n >= 8:
            for i in range(8, n+1):
                for j in range(2, i-1):
                    dp[i] = max(dp[i], dp[i-j] * j)
        return dp[n]

    def cuttingRope2(self, n: int) -> int:
        # 还是可以直接用动态规划的，dp[i] = max(dp[i], max(j * dp[i-j], j * (i-j)))
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(2, i):
                dp[i] = max(dp[i], max(j * dp[i-j], j * (i-j)))
        return dp[n]


if __name__ == '__main__':
    solu = Solution()
    ans = solu.cuttingRope2(10)
    print(ans)

