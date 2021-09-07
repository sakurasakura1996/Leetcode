"""
154. 寻找旋转排序数组中的最小值 II
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
注意数组中可能存在重复的元素。
示例 1：
输入: [1,3,5]
输出: 1
示例 2：
输入: [2,2,2,0,1]
输出: 0
说明：
这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
"""
# 有重复元素的话，对于剑指offer11那道简单题来说，我用暴力遍历法的话其实没有什么影响，照样通过了
# 对于原来二分搜索的方法来说，应该是有影响的了。
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 暴力遍历法，这种题遍历法又不太落后，直接暴力多好哈哈哈
        if not nums:
            return None
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return nums[0]

    def finMin_2(self, nums: List[int]) -> int:
        # 当然写了暴力遍历也不能说其他方法不会写啊，还是得熟悉熟悉
        n = len(nums)
        if n == 1 or nums[0] < nums[n - 1]:
            return nums[0]
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:    # 复杂度主要体现在这里了，我们把等于的情况单独拎出来将
                right -= 1
        return nums[left]

solu = Solution()
nums = [10,1,10,10,10]
ans = solu.findMin(nums)
print(ans)