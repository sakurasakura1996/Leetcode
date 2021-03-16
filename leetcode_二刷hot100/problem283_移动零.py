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
        if not nums or len(nums) == 1:
            return
        n = len(nums)
        # 遍历过程中，不断记录当前有几个0了
        count = 0
        for i in range(n):
            if nums[i] == 0:
                count += 1
            else:
                nums[i-count] = nums[i]
        for i in range(n-1, n-1-count, -1):
            nums[i] = 0

    def moveZeros2(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1



if __name__ == '__main__':
    solu = Solution()
    nums = [0, 1, 0, 3, 12]
    solu.moveZeroes(nums)
    print(nums)
