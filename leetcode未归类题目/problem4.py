"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# way 1
# 每次想解决办法时，第一反应都是直接最蠢的办法，把两个数组合并起来排序一下，然后找到中位数
# 后来想到的方法是，递归的找中间值，因为是有序数组，所以先各自找到数组的中位数，然后比较大小，如果相同。那么这就是最后的中位数
# 如果不相同，那么中位数应该是在中位数
from typing import List
import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

