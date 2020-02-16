"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 有一个想法是：直接把nums2放到nums1后面，然后直接对这m+n个元素进行快排
# way 1
# from typing import List
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         for i in range(len(nums2)):
#             nums1.insert(m+i,nums2[i])
#         # print(nums1)
#         # 然后就可以给前m+n个元素进行快速排序了。
#         nums1[:] = sorted(nums1[:m+n])    # 。。。python可以直接对其进行排序，但是时间复杂度并不是很高，因为并没有利用已经部分有序的特点
#         # print(nums1)


# way 2
# 一般而言，对于有序数组可以通过 双指针法 达到O(n + m)O(n+m)的时间复杂度。
# 最直接的算法实现是将指针p1 置为 nums1的开头， p2为 nums2的开头，在每一步将最小值放入输出数组中。
# 由于 nums1 是用于输出的数组，需要将nums1中的前m个元素放在其他地方，也就需要 O(m)O(m) 的空间复杂度。

# from typing import List
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         # first copy list nums1
#         temp = nums1[:m]
#         nums1 = []
#         # 然后可以对temp 和 nums2进行一个一个的比较，然后依次放入nums1中
#         left1 = 0
#         left2 = 0
#         while left1 < m and left2 < n:
#             if temp[left1] < nums2[left2]:
#                 nums1.append(temp[left1])
#                 left1 += 1
#             else:
#                 nums1.append(nums2[left2])
#                 left2 += 1
#         # 其中一个列表已经比较完了，那就把另一个剩下的直接全部插入nums1中
#         if left1 < m:
#             nums1[left1+left2:] = temp[left1:]
#         if left2 < n:
#             nums1[left1+left2:] = nums2[left2:]
#         print(nums1)


# way 3
# 第二个方法已经实现很好的时间复杂度，但是之前比较困扰的就是要先把nums1复制走，在从头开始比较，需要花费额外的空间复杂度，
# 题解中第三种方法还是  双指针法，但是是从后往前开始比较，并用一个 指针p来记录nums1从后往前插入的位置
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        right1 = m - 1
        right2 = n - 1
        p = m+n-1  # 也就是最大的元素应该插入的位置
        while right1 >= 0 and right2 >= 0:
            if nums1[right1] > nums2[right2]:
                nums1[p] = nums1[right1]
                right1 -= 1
            else:
                nums1[p] = nums2[right2]
                right2 -= 1
            p -= 1
        # if right1 >= 0 : 这种情况不需要处理啊，直接就是对的
        nums1[:right2+1] = nums2[:right2+1]
        print(nums1)
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solu = Solution()
solu.merge(nums1,3,nums2,3)
