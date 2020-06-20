"""
面试题08.01 三步问题
这道题我当时考研机试时做过，当时本身就不觉得这题难，但是败在了这个傻逼取模上
我一直搞不懂这是啥意思。原来是每次结果都要取模，因为你并不知道啥时候这个结果会超过上限

三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，
你需要对结果模1000000007。
示例1:
 输入：n = 3
 输出：4
 说明: 有四种走法
"""
class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000007
        return dp[n]

solu = Solution()
n = 3
ans = solu.waysToStep(n)
print(ans)
