""""
5440. 数组异或操作  显示英文描述
通过的用户数 0
尝试过的用户数 0
用户总通过次数 0
用户总提交次数 0
题目难度 Easy
给你两个整数，n 和 start 。
数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。
请返回 nums 中所有元素按位异或（XOR）后得到的结果。
示例 1：
输入：n = 5, start = 0
输出：8
解释：数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
     "^" 为按位异或 XOR 运算符。
"""
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2*i for i in range(n)]
        for i in range(1,n):
            nums[i] = nums[i]^nums[i-1]
        return nums[n-1]

solu = Solution()
ans = solu.xorOperation(10, 5)
print(ans)
