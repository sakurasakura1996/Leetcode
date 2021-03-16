"""
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
提示：
1 <= nums.length <= 50000
1 <= nums[i] <= 10000
"""
from typing import List
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # 采用双指针来做吧
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            while left <= n-1 and nums[left] % 2 == 1:
                left += 1
            while right >= 0 and nums[right] % 2 == 0:
                right -= 1
            if left <= right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp

        return nums

solu = Solution()
nums = [1, 3, 5]
ans = solu.exchange(nums)
print(ans)