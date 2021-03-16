"""
剑指 Offer 45. 把数组排成最小的数
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
示例 1:
输入: [10,2]
输出: "102"

示例 2:
输入: [3,30,34,5,9]
输出: "3033459"
提示:
0 < nums.length <= 100
说明:
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
"""
from typing import List

# 本质是排序问题，把nums转换为字符串之后，排好序。排序有传递性
# 但是单个字符串的排序并不行，应该是 x + y < y + x,那么 x排在前面，

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]
        for i in range(len(nums_str)-1):
            for j in range(i, len(nums_str)-1):
                if nums_str[i] + nums_str[j+1] > nums_str[j+1] + nums_str[i]:
                    nums_str[i], nums_str[j+1] = nums_str[j+1], nums_str[i]
        return "".join(nums_str)


if __name__ == '__main__':
    solu = Solution()
    nums = [3, 30, 34, 5, 9, 0]
    ans = solu.minNumber(nums)
    print(ans)
