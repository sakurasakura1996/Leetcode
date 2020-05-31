"""
滑动窗口的最大值
给定一个数组nums 和滑动窗口的大小k，请找出所有滑动窗口里的最大值
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
"""
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k
        ans = []
        while right <= len(nums):
            window = nums[left:right]
            cur_max = max(window)
            ans.append(cur_max)
            left += 1
            right += 1
        return ans