"""
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1
 说明:
你可以认为每种硬币的数量是无限的。
"""
from functools import lru_cache
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return -1
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin])
        return -1 if dp[amount] == amount+1 else dp[amount]

    def coinChange2(self, coins: List[int], amount:int) -> int:
        # 上面采用的是自底向上的动态规划，这里使用自顶向下的动态规划或者说 记忆化+递归的方法

        @lru_cache(None)
        def dp(num):
            if num < 0: return -1
            if num == 0: return 0
            ans = amount+1
            for coin in coins:
                # 这样的判断是有问题的，因为不是说num-coin >=0 就可以了，如果dp(num-coin)=-1咋办呢对吧
                # if num - coin < 0:
                #     continue
                # ans = min(dp(num-coin) + 1, ans)
                tmp = dp(num - coin)
                if tmp >= 0 and tmp < ans:
                    ans = tmp + 1
            return ans if ans < amount+1 else -1

        if amount < 1:return 0
        return dp(amount)





