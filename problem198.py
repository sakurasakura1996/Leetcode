"""
198 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋
在同一晚上被小偷闯入，系统会自动报警。给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""
# from typing import List
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         sum_1 = 0
#         sum_2 = 0
#         for i in range(len(nums)):
#             if i%2 == 0:
#                 sum_1 += nums[i]
#             else:
#                 sum_2 += nums[i]
#         return max(sum_1, sum_2)
# 写出上面的代码简直太菜了啊大兄弟，经过思考之后想用动态规划来做了，肯定可以这样做，但是心里在想是否把题目考虑复杂了。
# way1 动态规划
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 还要判断长度是否可能为0
        dp = [[0, 0] for _ in range(len(nums))]   # 第一个数是存没偷的最大值，第二个数是存偷了的最大值
        # 上面可以简化的，没必要耗费这么多空间，甚至O（n）的空间都不需要，只需要 O（1）空间，只需要存储最近的两个值就可以了
        dp[0][0] = 0
        dp[0][1] = nums[0]
        # 注意初始条件只需要交代0就可以了，不然会出现数组越界的问题，因为输入案例可能长度就只有1
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[len(nums)-1][0], dp[len(nums)-1][1])

# 动态规划简化版
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)

        return second


solu = Solution()
nums = [1]
ans = solu.rob(nums)
print(ans)