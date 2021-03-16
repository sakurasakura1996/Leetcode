"""
300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1
提示：
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
进阶：
你可以设计时间复杂度为 O(n2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?
"""
# 第一眼看到题目想到的方法有动态规划和滑动窗口法，然后用动态规划写了一下。
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 动态规划方法来做，时间复杂度是 O(n^2)，空间复杂度是O(N)，还有方法可以将时间复杂度降低到O(nlogn)
        n = len(nums)
        dp = [1] * n
        # dp[i]表示以i结尾的子序列最长的值
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        #


if __name__ == '__main__':
    solu = Solution()
    nums = [7,7,7,7,7,7,7]
    ans = solu.lengthOfLIS(nums)
    print(ans)

