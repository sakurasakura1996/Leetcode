from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 思路倒不是很难，可以用动态规划来做，之前自己想的是将第一个元素也添加到数组的最后一个
        n = len(nums)

        def my_rob(nums):
            length = len(nums)
            if not nums:
                return 0
            if length == 1:
                return nums[0]
            dp = [0] * length
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, length):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return dp[length-1]

        if n == 1:
            return nums[0]
        else:
            return max(my_rob(nums[1:]), my_rob(nums[:-1]))

if __name__ == '__main__':
    solu = Solution()
    nums = [0]
    ans = solu.rob(nums)
    print(ans)