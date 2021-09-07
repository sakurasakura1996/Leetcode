"""
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
提示：
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        nums.sort()
        ans = sum(nums[:3])

        for first in range(nums_len):
            if first > 0 and nums[first] == nums[first-1]:
                # 新遍历到的数字和上一个first数字相同，就不用管了
                continue
            second = first + 1
            third = nums_len - 1
            while second < third:
                s = nums[first] + nums[second] + nums[third]
                if s == target:
                    return target
                if abs(s - target) < abs(ans - target):
                    ans = s
                if s > target:
                    third_2 = third - 1
                    while second < third_2 and nums[third_2] == nums[third]:
                        third_2 -= 1
                    third = third_2
                else:
                    second_2 = second + 1
                    while second_2 < third and nums[second_2] == nums[second]:
                        second_2 += 1
                    second = second_2

        return ans
