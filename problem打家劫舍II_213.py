"""
213. 打家劫舍 II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
示例 1:
输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:
输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""
# 这是打家劫舍的第二道题，第一道题是problem198，本题将原来的数组改成了数组首尾相接。原理相同
# 自己好蠢啊，简单的举一反三都搞不出来，这道题可以拆解成求解两次198的解法
# 如果第一个房子不偷窃，那么就是nums[1:]
# 如果最后一个房子不偷窃，那么就是nums[:-1]。
# 注意一定是讨论第一个房子不偷窃和最后一个房子不偷窃的方式
# 而不是讨论第一个房子偷窃和不偷窃的方式，因为第一个房子偷窃了，那第二个房子还是有羁绊约束啊
from typing import List
class Solution:
    def rob1(self, nums:List[int])->int:
        if not nums:
            return 0
        n = len(nums)
        dp = [[0,0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1],dp[i-1][0])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[n-1][0], dp[n-1][1])


    def rob(self, nums:List[int])->int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))


solu = Solution()
nums = [1]
ans = solu.rob(nums)
print(ans)
