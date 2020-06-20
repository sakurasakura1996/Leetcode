""""
746.使用最小花费爬楼梯
数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

"""
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_len = len(cost)
        if cost_len == 2:
            return min(cost[0], cost[1])
        ans = [0] * (cost_len+1)
        ans[0] = 0
        ans[1] = 0
        ans[2] = min(cost[0], cost[1])
        for i in range(2, cost_len):
            ans[i+1] = min(ans[i]+cost[i], ans[i-1]+cost[i-1])
        return ans[cost_len]


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
solu = Solution()
ans = solu.minCostClimbingStairs(cost)
print(ans)