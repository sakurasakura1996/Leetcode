"""
53.最大子序和
给定一个整数数组nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大值和
示例
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
这道题和面试题中的42是同一题
"""
# 这道题我的第一反应应该是用滑动窗口方法，但是做这题时给到的标签是动态规划啊，先自己做做看吧
# from typing import List
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         # 搞了半天感觉滑动窗口确实做不了
#         # 仔细想了下，这属于动态规划的经典题目 不过dp数组的想法也要仔细思考注意下
#         # dp[i]表示的是以位置i为结尾字符所有子区间中最大的值，最大值所代表的子区间必须包含这个值
#         # 这样想：你总有一个最大值的子区间，他也肯定以某一个位置的值为末尾，那我这样指定dp数组的含义肯定是可以的
#         import sys
#         dp = [-sys.maxsize-1 for _ in range(len(nums))]
#         dp[0] = nums[0]
#         for i in range(1,len(nums)):
#             # if nums[i] >= 0:
#             #     dp[i] = dp[i-1]+nums[i]
#             # elif dp[i-1]>=0:
#             #     dp[i] = dp[i-1] + nums[i]
#             # else:
#             #     dp[i] = nums[i]
#             # 上面这种判断方式不如下面的简洁,判断无关nums[i]的正负的
#             if dp[i-1] < 0:
#                 dp[i] = nums[i]
#             else:
#                 dp[i] = dp[i-1]+nums[i]
#         return max(dp)

# way2 题目中说你实现了O(n)复杂度的解法之后，还让你试试更为精妙的分治法求解
# 分治法，分而治之。把一个大问题分成两个或者多个小问题来求解。
# 这里我还是看了别人的分析才搞出来的
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        center = int(len(nums)/2)
        left_max = self.maxSubArray(nums[0:center])
        right_max = self.maxSubArray(nums[center:len(nums)])

        # 还有可能最大区间是横跨了中间值的两边
        # max_left = 0
        # max_right = 0  有负数，初始的最大值要赋值成最小值，应该是负的最大值
        import sys
        max_left = -sys.maxsize - 1
        max_right = max_left
        sum = 0
        for i in range(center-1, -1, -1):
            sum += nums[i]
            if sum > max_left:
                max_left = sum

        sum = 0
        for i in range(center, len(nums), 1):
            sum += nums[i]
            if sum > max_right:
                max_right = sum
        return max(left_max, right_max, max_left+max_right)






solu = Solution()
nums = [-2, -1]
ans = solu.maxSubArray(nums)
print(ans)

