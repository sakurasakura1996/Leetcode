"""
416. 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].

示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
"""
# 做这题是已知道要用动态规划的方法了。在做494题的时候，不会写，别人的题解写到了这道题。所以顺带来做一做
# 这道题是动态规划内的典形问题原型-背包问题。背包体现在这个数组总和上，因为背包能够容纳下的重量是给定的，题目中的数组元素和也是固定的
# 现在要分成两个子集，也就是，我要挑一部分放到背包中，只不过现在的背包容量是数组总和的一半，而且要求拿到的东西恰好装满这个背包。其实就是
# 动态规划中的背包问题，做完这个题目可以去仔细归纳一下 动态规划内的 背包问题

from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        total = nums_sum // 2
        nums_len = len(nums)
        dp = [[False] * (total+1) for _ in range(nums_len+1)]
        # dp[i][j]表示数组前i个数字，是否可以选择一部分数字是他们的和加起来等于j，
        # 处理边界特殊情况
        for i in range(nums_len+1):
            dp[i][0] = True
        for i in range(1,nums_len+1):
            for j in range(1,total+1):
                if j-nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[nums_len][total]

# 注意，此方法中的的空间复杂度可以进行优化，那就是压缩dp数组变为一维。
    def canPartition_2(self, nums: List[int]) -> bool:
        # 因为dp数组填表格中的值时，其实我们填这一行只用到上一行的数据，那么其实我们如果只维护两行数值，就可以节省空间复杂度啦
        # 不对，可以只用一行数组就行了，二行不还是二维的吗，
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        total = nums_sum // 2
        nums_len = len(nums)
        dp = [False] * (total+1)
        dp[0] = True   # 这个数组中的索引相当于二维数组中的j，第二个维度
        for i in range(nums_len):
            # 注意j要从后向前遍历
            for j in range(total, -1, -1):
                if j-nums[i] >=0:
                    dp[j] = dp[j] or dp[j-nums[i]]
        return dp[total]




solu = Solution()
nums = [1, 2, 3, 5]
ans = solu.canPartition_2(nums)
print(ans)



