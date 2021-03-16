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
# 因为是二刷，所以当时这道题目没做出来，有点印象，我们不能使用简单的字符序列排序，这里有一个技巧就是：
# if x + y < y + x ->  x < y
# 所以我们只需要排个序就行
from typing import List
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        if not nums:
            return
        nums_str = [str(num) for num in nums]
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums_str[j] + nums_str[j+1] > nums_str[j+1] + nums_str[j]:
                    nums_str[j], nums_str[j+1] = nums_str[j+1], nums_str[j]
        return "".join(nums_str)

# 这里我再记录一下冒泡排序吧，严格的说法，冒泡排序是比较类排序，通过不断的相邻元素的比较，每一轮可以让一个元素知道自己的位置在哪。
# 那我们最好在脑海中形成冒泡排序的规范写法吧：
# for i in range(n):
#     for j in range(n-i-1):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]


if __name__ == '__main__':
    solu = Solution()
    nums = [2, 1]
    ans = solu.minNumber(nums)
    print(ans)



