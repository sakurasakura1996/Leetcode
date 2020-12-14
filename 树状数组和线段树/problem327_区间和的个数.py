"""
327. 区间和的个数
给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

说明:
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

示例:

输入: nums = [-2,5,-1], lower = -2, upper = 2,
输出: 3
解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
"""
# 如果用暴力法的话，那么复杂度就是O(N^2),这里采用树状数组来解决问题，可以将时间复杂度降低到O(NlogN)
# 区间和问题，多想想是否可以用树状数组和线段树来解决问题。
from typing import List
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        n = len(nums)
        tree = [0] * n  # 树状数组


    def lowbit(self, x):
        return x & (-x)

    def update(self, ):

    def query(self, ):



