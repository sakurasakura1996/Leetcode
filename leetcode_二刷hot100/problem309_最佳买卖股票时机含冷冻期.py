from typing import List
class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [[0, 0, 0] for _ in range(n)]
        # 边界初始化 ans[i][0],ans[i][1], ans[i][2]分别表示处于买入，卖出，冷冻期的状态
        ans[0][0] = -nums[0]


        for i in range(1, n):
            for j in range(i):
                ans[i][1] = max(ans[i][1], ans[])
