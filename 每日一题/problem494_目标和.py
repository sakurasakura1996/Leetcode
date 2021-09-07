from typing import List
from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 第一种想到的方法肯定是回溯法，但是，这道每日一题，官方其实更想让你考虑到动态规划解法，2021.6月份的每日一题主题应该是动态规划
        # 我们都来写一遍
        # 回溯法: 竟然超时了，我们需要进行优化，剪枝看看
        ans = 0

        def backtrace(cur, path, summ, target):
            nonlocal ans
            if not path and summ == target:
                ans += 1
            elif path:
                num = path[0]
                cur.append(num)
                summ += num
                path = path[1:]
                backtrace(cur, path, summ, target)
                summ -= 2 * num
                backtrace(cur, path, summ, target)
        backtrace([], nums, 0, target)
        return ans

    @lru_cache(None)
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        # 回溯法能通过版本，妈的，通过个毛线
        ans = 0
        n = len(nums)
        def backtrace(index: int, summ: int) -> None:
            nonlocal ans
            if index == n and summ == target:
                ans += 1
            if index != n:
                backtrace(index+1, summ+nums[index])
                backtrace(index+1, summ-nums[index])
        backtrace(0, 0)
        return ans

    def findTargetSumWays3(self, nums:List[int], target: int) -> int:
        # 动态规划解法  dp[i][j] 表示前i个数，组成和为j的组合数
        # 那么，dp[i][j] =
        m = len(nums)
        summ = sum(nums)
        diff = summ - target
        if diff < 0 or diff%2 != 0:
            return 0
        neg = diff // 2
        dp = [[0] * (neg+1) for _ in range(m+1)]
        dp[0][0] = 1
        for i in range(1, m+1):
            num = nums[i-1]
            for j in range(neg+1):
                dp[i][j] = dp[i-1][j]
                if j >= num:
                    dp[i][j] += dp[i-1][j-num]
        return dp[m][neg]





if __name__ == '__main__':
    solu = Solution()
    nums = [1]
    target = 1
    ans = solu.findTargetSumWays2(nums, target)
    print(ans)



