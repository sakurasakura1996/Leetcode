"""
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
限制：
0 <= 数组长度 <= 50000
注意：本题与主站 34 题相同（仅返回值不同）
"""
from typing import List
from collections import Counter
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(N) 时间复杂度
        num_counter = Counter(nums)
        if target in num_counter.keys():
            return num_counter[target]
        else:
            return 0

    def search2(self, nums: List[int], target: int) -> int:
        # 题目中有排序的关键字，可以用二分法查找到 target的左边界left，和右边界right
        # 平常我们都是用二分法找到某一个数的位置，现在找到左右边界，怎么找呢？
        if not nums:
            return 0
        n = len(nums)
        left = 0
        right = n
        # 左边界，右边界得找两遍
        # 先找左边界
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        left_target = left
        # 再找右边界
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        right_target = left - 1
        # print(left_target, right_target)
        if left_target < n and nums[left_target] == target and nums[right_target] == target:
            return right_target - left_target + 1
        else:
            return 0


if __name__ == '__main__':
    solu = Solution()
    nums = [5,7,7,8,8,10]
    target = 6
    ans = solu.search2(nums, target)
    print(ans)