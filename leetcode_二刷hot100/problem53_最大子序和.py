from typing import List

# 如果已经实现复杂度为O(n)的解法，尝试使用更为精妙的 分治法 求解
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [float('-inf')] * (len(nums))
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)


if __name__ == '__main__':
    solu = Solution()
    nums = [0]
    ans = solu.maxSubArray(nums)
    print(ans)

