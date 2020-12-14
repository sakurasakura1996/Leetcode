"""
前缀和的思想，我们可以存储奇偶元素的差值，而不一定非要计算和
"""
from typing import List
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        # dp定义为奇数和减偶数和
        for i in range(1, n+1):
            dp[i] = dp[i-1] + (-nums[i-1] if i%2 else nums[i-1])

        ans = 0
        for i in range(1, n+1):
            if dp[i-1] == dp[n] - dp[i]:
                ans += 1
        return ans

solu = Solution()
nums = [1,2,3]
ans = solu.waysToMakeFair(nums)
print(ans)

