"""
给你一个整数数组 nums 和一个整数 target 。
请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。
由于答案可能很大，请将结果对 10^9 + 7 取余后返回。
示例 1：
输入：nums = [3,5,6,7], target = 9
输出：4
解释：有 4 个子序列满足该条件。
[3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
"""

from typing import List
class Solution:
    def subNum(self, nums: List[int])-> int:
        # 根据这个nums数组，返回能组成多少个子数组满足情况，nums默认有序的
        nums_len = len(nums)

    def numSubseq(self, nums: List[int], target: int) -> int: