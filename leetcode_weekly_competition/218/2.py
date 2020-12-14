from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            if nums[left] + nums[right] == k:
                ans += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
        return ans

solu = Solution()
nums = [3,1,3,4,3]
k = 6
ans = solu.maxOperations(nums, k)
print(ans)

