"""
剑指 Offer 53 - II. 0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
示例 1:
输入: [0,1,3]
输出: 2
示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
限制：
1 <= 数组长度 <= 10000
"""
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 二分查找
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid+1
            else:
                right = mid - 1
        return left

solu = Solution()
nums = [0,1,2,3,4,5,6,7,9]
ans = solu.missingNumber(nums)
print(ans)
