"""
283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                if i == pointer:
                    pointer += 1
                else:
                    nums[pointer] = nums[i]
                    nums[i] = 0
                    pointer += 1
        print(nums)


if __name__ == '__main__':
    solu = Solution()
    nums = [0,1,0,3,12]
    solu.moveZeroes(nums)

