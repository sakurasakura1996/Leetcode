""""
70.爬楼梯
经典问题。我们可以用动态规划或者递归，但是递归重复计算过多了

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [0] * (n+2)
        ans[1] = 1
        ans[2] = 2
        for i in range(3, n+1):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[n]


solu = Solution()
ans = solu.climbStairs(2)
print(ans)
