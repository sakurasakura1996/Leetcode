# 动态规划的时间复杂度是O(N^2),那你能将时间复杂度降到O(NlogN)吗
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 感觉这两天的做题状态实在太差了啊，动态规划解法可能不是最好的，但是你最起码能看到题目就想到用动态规划啊
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        print(dp)
        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        # 贪心算法+二分查找，我们维护状态数组tail，它的长度就是最长上升子序列的长度。tail[i]表示：长度为 i+1 的所有上升子序列的结尾的最小值
        n = len(nums)

        if n < 2:
            return n
        tail = [nums[0]]
        for i in range(1, n):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue

            # 使用二分查找法，在tail数组中查找到第1个大于等于nums[i]的元素，尝试让那个元素更小
            left = 0
            right = len(tail) - 1
            while left < right:
                mid = left + (right-left) // 2
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = nums[i]
        return len(tail)


if __name__ == '__main__':
    solu = Solution()
    nums = [10,9,2,5,3,4]
    ans = solu.lengthOfLIS(nums)
    print(ans)


