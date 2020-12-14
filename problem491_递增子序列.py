"""
491. 递增子序列
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
示例:
输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:
给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
"""
# 如果一个序列是递增的（包括相等），那么它的所有子序列除了空和只有一个元素，其他的应该都满足要求，那么我们可以把一个nums序列拆分啊
# 拆分成多个递增序列，如果整个nums数组是递增的，那就是一个序列。
from typing import List
from collections import deque
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(nums, track):
            if len(track) >=2 and track not in ans:
                ans.append(track)
            if not nums:
                return

            for i in range(len(nums)):
                # 判断track最后一个 是否小于 数组中的想要进来的数
                # 就是track是一个递增数组 进来的数必须大于track数组最后一个属
                if not track or nums[i] >= track[-1]:
                    backtrack(nums[i+1:], track+[nums[i]])

        backtrack(nums, [])
        return ans





