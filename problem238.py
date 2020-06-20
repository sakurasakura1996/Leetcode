"""
除自身以外数组的乘积
给你一个长度为n的整数数组nums，其中 n>1,返回输出数组output，其中output[i]等于nums中除nums[i]之外其余各元素的乘积
实例
输入：[1,2,3,4]
输出：[24,12,8,6]
提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内
要求:不要使用除法，且在 O(n)时间复杂度内完成
进阶:你可以在常数空间复杂度内完成这个题目吗？
"""
# 晃着一看，第一想到的肯定就是把整个数组乘起来，然后分别除一下，思路简单，而且复杂度也不高
# 但是题目明确了不准用除法，一时间想不到用什么方法来做了。。。
# 除法
# from typing import List
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         mul = 1
#         for i in range(len(nums)):
#             mul *= nums[i]
#
#         for i in range(len(nums)):
#             nums[i] = int(mul/nums[i])
#         return nums


# way2 双指针也就是双向遍历一遍
#　这个题目想起来可能以前碰到过，所以隐约记得从两边开始遍历一遍
# 从左往右 和从右往左各遍历一遍，记住从开头到当前节点（不包含本节点）的乘积，然后对应位置再乘起来
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1 = [1 for _ in range(len(nums))]
        nums2 = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            nums1[i] = nums1[i-1] * nums[i-1]
        for j in range(len(nums2)-2, -1, -1):
            nums2[j] = nums2[j+1] * nums[j+1]
            # nums2[j] = nums2[j] * nums1[j]
        for i in range(len(nums)):
            nums[i] = nums1[i] * nums2[i]
        return nums

solu = Solution()
nums = [1,2,3,4]
ans = solu.productExceptSelf(nums)
print(ans)
