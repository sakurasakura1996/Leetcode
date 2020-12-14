"""
496. 下一个更大元素 I
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。

示例 2:
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
提示：
nums1和nums2中所有元素是唯一的。
nums1和nums2 的数组大小都不超过1000。
"""
from typing import List
class Solution:
    # 方法一：题目定位为简单题，我们直接用暴力法就可以解决。
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = [-1] * n1
        for i in range(n1):
            idx = nums2.index(nums1[i])
            for j in range(idx, n2):
                if nums2[j] > nums1[i]:
                    ans[i] = nums2[j]
                    break
        return ans

    # 方法二：使用单调栈的思想去解决它
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 因为单调栈的作用主要就是找到该元素前一个或者后一个比它大或者比它小的值，所以我们尝试用单调栈来解决该问题。
        # 首先，因为题目是要找到数组1中的每个元素在数组2中对应位置的右边比它大的第一个元素。
        # 分析应该是从右向左遍历的一个递减栈
        n1 = len(nums1)
        n2 = len(nums2)
        stack = list()
        ans = {}
        for i in range(n2-1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            ans[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        ret = []
        for i in range(n1):
            ret.append(ans[nums1[i]])
        return ret

solu = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
ans = solu.nextGreaterElement2(nums1, nums2)
print(ans)




