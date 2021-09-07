"""
494.目标和
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
示例：
输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
一共有5种方法让最终目标和为3。
提示：
数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。
"""
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            if S == 0:
                return 1
            else:
                return 0

        if len(nums) == 1 and nums[0] == S:
            if S == 0:
                return 2
            else:
                return 1
        num = nums[0]
        sum_1 = self.findTargetSumWays(nums[1:], S-num)
        sum_2 = self.findTargetSumWays(nums[1:], S+num)
        return sum_1 + sum_2

# 上面这种写法，还不如暴力法清晰，因为它还是 O(2^N)的复杂度，这是没有实际用处的，提交时超时，还不知道是否对
# 做这道题是看到公众号讲回溯和动态规划时举例的一道题，其中动态规划的思路实在是妙。这道题是一道常见的背包问题。
# 这道题首先可以转换为子集划分问题，子集划分问题又是一个经典的动态规划问题。
# 子集划分问题的思考在于，因为数字前面只能选择 + 或者 -，那么把填+的放在前面，把填-的放在后面。那么就是
#　sum(A) - sum(B) = target  ->  sum(A) = target + sum(B)   -> sum(A) + sum(A) = target + sum(nums)
# 进而得到sum(A) = (target+sum(nums))/2,target和sum(nums)都是已知的，这个时候，问题就转换为了nums数组中哪些数的前面填+。使得
# sum(A) = (target+sum(nums))/2。这个时候，问题就转换为我们比较熟悉的动态规划经典思路了。
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        nums_len = len(nums)
        nums_sum = sum(nums)
        target = (S+nums_sum)
        if target % 2 != 0 or target < 0 or nums_sum < S:
            return 0
        target = target // 2

        dp = [0] * (target+1)
        dp[0] = 1  # 对应二维数组中的dp[...][0]表示什么target = 0满足的方法数，什么都不选，方法数为1
        for i in range(nums_len):
            # 压缩空间的话，记得内重循环要倒序进行（还是要看递推公式的情况）
            for j in range(target, nums[i]-1, -1):   # 这里范围缩减到nums[i]-1更好，因为你后面反正会要求j-nums[i]>=0
                # 所以你往下都是无用功，但是我觉得这也不会损失太多吧。然后我把这个nums[i]-1和-1的都提交了一遍，都通过了，这特么什么鬼。
                # 后面看了提交记录，发现代码区别在于上面的第52行，我当时只写了target不能为奇数，没有考虑target<0 和 nums_sum<S的问题。
                if j - nums[i] >= 0:
                    dp[j] = dp[j] + dp[j-nums[i]]
        return dp[target]
# 为什么这个方法竟然还会超出时间限制啊，我日，仔细分析下看看
# 我发现，上面代码虽然没有报错，但是有问题，因为这里的S可能是负数呢？那么你判断 j-nums[i]>=0是不是存在问题。注意到题目中提示初始的数组和
# 不超过1000，数组非空，且长度不会超过20.那么我们可以在索引的基础上加上1000吗
# 搞了半天，看了别人的题解，我发现我和别人的代码只有一个地方不一样，就是上面的第60行






nums = [25,29,23,21,45,36,16,35,13,39,44,15,16,14,45,23,50,43,9,15]
S = 32
solu = Solution()
ans = solu.findTargetSumWays(nums, S)
print(ans)
