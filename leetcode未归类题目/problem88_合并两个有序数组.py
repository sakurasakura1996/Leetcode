"""
88. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
提示：
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = [0] * (m+n)
        p1, p2, tmp = 0, 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                temp[tmp] = nums1[p1]
                p1 += 1
                tmp += 1
            else:
                temp[tmp] = nums2[p2]
                p2 += 1
                tmp += 1
        if p1 < m:
            while p1 < m:
                temp[tmp] = nums1[p1]
                p1 += 1
                tmp += 1
        else:
            while p2 < n:
                temp[tmp] = nums2[p2]
                p2 += 1
                tmp += 1
        for i in range(m+n):
            nums1[i] = temp[i]

# 上面的时间复杂度可以了，但是空间复杂度是O（m+n），可以优化，我们只用O（m)也就是把nums1的部分用一个数组存起来，但是这个还是不够好，我们可以用
# O(1)的空间复杂度来完成它。那就是从后往前赋值，先比较两个有序数组中最大的值，然后，到最后，只需要把nums2余下的部分塞入nums1的前面就可以了。
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m-1, n-1, m+n-1
        while p1 >=0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1
        # 最后,可能还有一部分没有复制到nums1，我们只需要管nums2没有赋值的情况，因为如果nums2赋值空了，nums1就不用管了
        nums1[:p2+1] = nums2[:p2+1]

# 提交之后，后面的方法反而更加耗时，空间用的更多，我只能说leetcode就尼玛离谱
