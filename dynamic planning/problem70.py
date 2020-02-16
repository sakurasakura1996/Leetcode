""""
爬楼梯 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""

class Solution:
    def climbStairs(self, n: int)->int:
        ans = [0,1,2]
        if n == 1 or n == 2:
            return ans[n]
        else:
            for i in range(3,n+1):
                num = ans[i-1] + ans[i-2]
                ans.append(num)
            return ans[n]


solu = Solution()
ans = solu.climbStairs(4)
print(ans)