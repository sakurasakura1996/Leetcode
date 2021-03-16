"""
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。
示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3

示例 3：
输入：nums = [1,1]
输出：1

示例 4：
输入：nums = [1,1,2]
输出：1
提示：
2 <= n <= 3 * 104
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
进阶：
如何证明 nums 中至少存在一个重复的数字?
你可以在不修改数组 nums 的情况下解决这个问题吗？
你可以只用常量级 O(1) 的额外空间解决这个问题吗？
你可以设计一个时间复杂度小于 O(n2) 的解决方案吗？
"""
# 这类题目已经看到很多次了，而且难度都还是中等题，主要问题进阶问题，让你只有O(1)的空间复杂度，不要用额外的内存空间来存储。
# 如果没有限制，这类题目很好写，直接用一个counter计数就可以了。但是要求O(1)空间复杂度来完成。
from typing import List
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 空间复杂度为O（n)，不符合要求
        nums_counter = Counter(nums)
        for key, value in nums_counter.items():
            if value > 1:
                return key

    def findDuplicate2(self, nums: List[int]) -> int:
        # 排序的话，时间复杂度为O(nlogn),空间复杂度为O(1),满足了要求，但是nums数组变动了，所以还是不能完全符合题意。
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]

    def findDuplicate3(self, nums: List[int]) -> int:
        # 那么到底什么方法才是满足题意的呢，我只记得大概是用位运算来做。一直没有搞懂过
        # 这道题主流解法还真不是位运算，是二分法。。。。题眼是 数值范围为 1到n





if __name__ == '__main__':
    solu = Solution()
    nums = [3,1,3,4,2]
    ans = solu.findDuplicate(nums)
    print(ans)