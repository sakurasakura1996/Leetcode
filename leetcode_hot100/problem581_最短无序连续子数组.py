"""
581. 最短无序连续子数组
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
请你找出符合题意的 最短 子数组，并输出它的长度。
示例 1：
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

示例 2：
输入：nums = [1,2,3,4]
输出：0

示例 3：
输入：nums = [1]
输出：0
提示：
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？
"""
# 如果不是要求O(n)的时间复杂度，那么直接排个序然后对比下就ok了，我们先写下
from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums.copy())
        if nums == sorted_nums:
            return 0
        n = len(nums)
        left, right = 0, n-1
        for i in range(n):
            if nums[i] != sorted_nums[i]:
                left = i
                break
        for j in range(n-1, -1, -1):
            if nums[j] != sorted_nums[j]:
                right = j
                break

        return right - left + 1

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        # show my code how to achieve O(n)'s solution
        n = len(nums)
        max_num = nums[0]
        right = 0
        for i in range(n):
            # 原理上，我们就是要找到一个左右区间，这个区间左边的数都比区间内的数小，右边的数都闭它大
            # 那么我们要找到这个区间的左右边界。
            if nums[i] >= max_num:
                max_num = nums[i]
            else:
                right = i  # right右边的数竟然还比max_num要大，那说明这个数也在乱序区间内啊。
        left = n
        min_num = nums[-1]
        for i in range(n-1, -1, -1):
            if nums[i] <= min_num:
                min_num = nums[i]
            else:
                left = i
        return right - left + 1 if (right - left + 1 > 0) else 0




if __name__ == '__main__':
    solu = Solution()
    nums = [2, 1]
    ans = solu.findUnsortedSubarray(nums)
    print(ans)

