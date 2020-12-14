from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums%2 != 0:
            return False;
        n = len(nums)

        dp = [[False] * (sums//2+1) for _ in range(n+1)]

        # 初始化边界,默认都是False
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, (sums//2)+1):
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-nums[i-1]]) if (j - nums[i-1]) >= 0 else dp[i-1][j]

        return dp[n][sums//2]


solu = Solution()
nums = [1, 5, 11, 5]
ans = solu.canPartition(nums)
print(ans)

