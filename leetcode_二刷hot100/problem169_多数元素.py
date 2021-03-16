"""
169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1：
输入：[3,2,3]
输出：3

示例 2：
输入：[2,2,1,1,1,2,2]
输出：2
进阶：
尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
"""
# 题解中写了四五种方法，我们一一了解看看
from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(n)时间复杂度，O(n)空间复杂度，空间复杂度不满足进阶要求
        n = len(nums)
        nums_counter = Counter(nums)
        for key, value in nums_counter.items():
            if value > n//2:
                return key

    def majorityElement2(self, nums: List[int]) -> int:
        # O(nlogn)时间复杂度， O(logn)空间复杂度, 使用排序算法，先排个序，然后中间数肯定是众数
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement3(self, nums: List[int]) -> int:
        # 随机化，因为超过一半的数组下标被众数占据了，这样我们随机挑选一个下标对应的元素并验证，有很大概率能找到众数
        majority_count = len(nums) // 2
        import random
        while True:
            candidate = random.choice(nums)
            if sum(1 for item in nums if item == candidate) > majority_count:
                return candidate
            # 随机化方法，是可以实现O(n)时间复杂度，O(1)空间复杂度的，时间复杂度的计算要通过概率学来计算下。

    def majorityElements4(self, nums: List[int]) -> int:
        # 分治法：思想就是，如果a是数组nums的众数，那么如果nums分成两半，那么a至少是其中一半数组的众数，反证法可以证明之。
        # 时间复杂度O(nlogn) 空间复杂度O(logn)

       def majority_element_rec(lo, hi) -> int:
            if lo == hi:
                return nums[lo]

            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            if left == right:
                return left

            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right
       return majority_element_rec(0, len(nums) - 1)

    def majorityElements5(self, nums: List[int]) -> int:
        # Boyer-Moore算法，如果遍历到众数，我们+1，如果不是众数，我们就-1，那么最后下来，结果值肯定还是正数，这样的话，我们就遍历一遍是否可以呢
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

