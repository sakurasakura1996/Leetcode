"""
303.区域和检索-数组不可变
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
示例：
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
"""
# 题目提到假设数组不可变，同时 会多次调用 求和函数，所以如果我们每次调用求和函数都遍历求和的话应该是比较耗时的，
# 可以用动态规划的方法来做，我们可以用一个 一维的dp数组，dp[i]来存储(0，i)的总和，然后每次调用求和函数只需要相减一下即可
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dp = [0 for _ in range(len(nums))]
        ans = 0
        for i in range(len(nums)):
            ans += nums[i]
            self.dp[i] = ans

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i] + self.nums[i]


nums = [-2, 0, 3, -5, 2, -1]
solu = NumArray(nums)
