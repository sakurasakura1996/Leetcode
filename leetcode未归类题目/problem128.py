"""
128最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。
示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""
# 想到一个比较蠢的方法，我创建一个数组中最大值长度的数组，然后遍历一遍原数组
# 如果出现了则在对应位置赋值1，然后在遍历的过程中找到最大的连续1串，但这个
# 并不止O(N)的复杂度。后来的想法是可不可以用一个有序字典来保存，但复杂度还是
# 不止O(N)复杂度。

# way1
# from typing import List
# from collections import OrderedDict
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         nums.sort()    # 总觉得这个方法并不是O(n)的时间复杂度，光这个排序就做不到O(N)的复杂度啊，快排都要nlogn
#         ans = 1
#         cur_ans = 1
#         for i in range(1,len(nums)):
#             if nums[i] != nums[i-1]:
#                 if nums[i] == nums[i-1]+1:
#                     cur_ans += 1
#                 else:
#                     ans = max(ans, cur_ans)
#                     cur_ans = 1
#         return max(ans, cur_ans)


# way2
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                cur_num = num
                cur_ans = 1
                while cur_num+1 in num_set:
                    cur_num += 1
                    cur_ans += 1
                ans = max(ans, cur_ans)
        return ans

# 在leetcode上提交之后，上述两个方法的用时和用的空间基本上差不多，然而我觉得应该第二个方法应该更好啊。
# 看题解上还有动态规划的解法。
# 这方法挺巧妙的。
class Solution(object):
    def longestConsecutive(self, nums):
        hash_dict = dict()

        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)

                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length

                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length

        return max_length



solu = Solution()
nums = [100, 4, 200, 1, 3, 2]
ans = solu.longestConsecutive(nums)
print(ans)

