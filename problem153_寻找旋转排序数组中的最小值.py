"""
153. 寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
你可以假设数组中不存在重复元素。
示例 1:
输入: [3,4,5,1,2]
输出: 1
示例 2:
输入: [4,5,6,7,0,1,2]
输出: 0
"""
# woca,这道题和剑指offer那道题差不多啊，只是不存在重复元素了，难度改为了中等，那就用二分法
# 不太一样，错误示例 有 [1,2]，那就是从1前面进行了旋转。
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]

    def findMin_2(self, nums: List[int]) -> int:
        # 运用二分法，降低时间复杂度,这个题二分搜索还是值得仔细考虑考虑的
        n = len(nums)
        if n == 1 or nums[0] < nums[n-1]:
            return nums[0]
        left = 0
        right = n-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]


solu = Solution()
nums = [4,5,6,7,0,1,2]
ans = solu.findMin_2(nums)
print(ans)


