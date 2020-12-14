"""
描述
给定一个无序数组，可能包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大
nums.size <= 500000 -10000 <= nums[i] <= 10000
示例
输入:  nums = [3,4,1,2]
输出: 24

"""
import sys
class Solution:
    def MaximumProduct(self, nums):
        n = len(nums)
        assert n >= 3
        max1 = -(sys.maxsize)
        max2 = -(sys.maxsize)
        max3 = -(sys.maxsize)
        min1 = sys.maxsize
        min2 = sys.maxsize
        # 找到数组中最大的前三个数和最小的后两个数
        for i in range(n):
            if nums[i] > max1:
                max3 = max2
                max2 = max1
                max1 = nums[i]
            elif nums[i] > max2:
                max3 = max2
                max2 = nums[i]
            elif nums[i] > max3:
                max3 = nums[i]
            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]
        # 判断多种情况
        if max1 <= 0:
            return max1 * max2 * max3
        elif max2 <= 0:
            return max1 * min2 * min1
        elif max3 <= 0:
            return max1 * min1 * min2
        else:
            return max(max1 * max2 * max3,max1*min1*min2)

solu = Solution()
nums = [0,1,4,-3]
ans = solu.MaximumProduct(nums)
print(ans)

