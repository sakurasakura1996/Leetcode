""""
problem209 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。
示例: 
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

"""
from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        nums_len = len(nums)
        left = 0
        right = 0
        cur_sum = 0
        window = []
        ans = len(nums)
        if sum(nums) < s:
            return 0
        while right < nums_len:
            window.append(nums[right])
            cur_sum += nums[right]
            right += 1
            while cur_sum >= s:
                ans = min(ans, len(window))
                window.remove(nums[left])
                cur_sum -= nums[left]
                left += 1
        return ans

solu = Solution()
s = 7
nums = [2, 3, 1, 2, 4, 3]
ans = solu.minSubArrayLen(s,nums)
print(ans)