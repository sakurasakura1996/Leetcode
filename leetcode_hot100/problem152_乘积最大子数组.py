"""
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
# 要不就暴力解法看看
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 暴力法超时了哈哈哈
        n = len(nums)
        ans = max(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n):
            tmp = nums[i]
            for j in range(i+1, n):
                tmp *= nums[j]
                dp[i][j] = tmp
                ans = max(ans, dp[i][j])
        return ans

    # def maxProduct2(self, nums: List[int]) -> int:
    #     # 这种方法最终没有想好
    #     n = len(nums)
    #     product = [nums[0]]
    #     cur = nums[0]
    #     for i in range(1, n):
    #         cur *= nums[i]
    #         product.append(cur)
    #     dp = nums.copy()
    #     for i in range(n):
    #         dp[i] = max(dp[i], product[i])
    #         for j in range(i):
    #             dp[i] = max(dp[i], product[i]/product[j])
    #             # 数组中有0怎么办呢
    #     return max(dp)

    def maxProduct3(self, nums: List[int]) -> int:
        # 用动态规划方法来写，但是我之前想过用它，问题是，没有搞懂其中的问题，比如说到了求dp[i]的时候，dp[i]的最大值并不能由dp[i-1]递推出来啊
        # 比如，nums=[-3, 2, 3, -4]，那么dp[2] = 6, dp[3]也要考虑到nums[0]的值，正好负负得正，从而得到更大的值，这点我是想到了，但是太蠢
        # 没有进一步思考如何解决这个问题，题解中交代的是我们维护两个值嘛，或者说维持两个dp嘛，一个最大值dp，一个最小值dp。
        # 最后提交通过了，但是效率不高
        n = len(nums)
        if n == 0:return 0
        if n == 1:return nums[0]
        maxAns = nums.copy()
        minAns = nums.copy()
        ans = nums[0]
        for i in range(1, n):
            maxAns[i] = max(maxAns[i], maxAns[i-1] * nums[i], minAns[i-1] * nums[i])
            minAns[i] = min(minAns[i], maxAns[i-1] * nums[i], minAns[i-1] * nums[i])
            ans = max(ans, maxAns[i], minAns[i])
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [2,3,-2,4]
    ans = solu.maxProduct4(nums)
    print(ans)


