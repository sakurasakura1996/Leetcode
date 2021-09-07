from typing import List
class Solution:
    # 这个题目的简单版主要就是简化了nums数组是递增的，数组中的值都互不相同了。思路肯定是二分
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid]:
                left += 1
                continue
            if nums[left] < nums[mid]:
                # mid 在左半部分中
                if nums[left] <= target < nums[mid]:  # 一定要注意这里的等于号，因为我们这时候关注的是right的进一步取值，左边是可以等于的
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # mid 在右半部分
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
