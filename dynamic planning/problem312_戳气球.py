"""
312. 戳气球
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表
和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。求所能获得硬币的最大数量。
说明:
你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:
输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0] * (n+2) for _ in range(n+2)]
        val = [1] + nums + [1]

        # 分析动态规划状态转移方程时，会得到，以往的遍历方式不能解决问题，所以要倒序遍历
        for i in range(n-1, -1, -1):
            for j in range(i+2, n+2):  # 这里的区间要注意分析，因为我们给nums数组左右各扩展了一位，但是这两个都不能取到
                for k in range(i+1, j):
                    # 注意这里的k选择的是最后一个戳破的气球，那么它的左右两边肯定都是边界，值为1了。
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + val[i]*val[k]*val[j])
        return dp[0][n+1]

    def maxCoins2(self, nums: List[int]) -> int:
        # 反向思考，原题目是每次戳破一个气球，那么我们反向思考为每次往其中加入一个气球。
        from functools import lru_cache
        n = len(nums)
        val = [1] + nums + [1]

        @lru_cache(None)
        def solve(i, j) ->int:
            if i >= j-1:return 0
            best = 0
            for k in range(i+1, j):
                best = max(best, solve(i, k) + solve(k, j) + val[i] * val[k] * val[j])
            return best
        ans = solve(0,n+1)
        return ans


solu = Solution()
nums = [3, 1, 5, 8]
ans = solu.maxCoins2(nums)
print(ans)

