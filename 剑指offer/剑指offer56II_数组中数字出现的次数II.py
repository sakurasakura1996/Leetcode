"""
剑指 Offer 56 - II. 数组中数字出现的次数 II
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
示例 1：
输入：nums = [3,4,3,3]
输出：4

示例 2：
输入：nums = [9,1,7,9,7,9,7]
输出：1
限制：
1 <= nums.length <= 10000
1 <= nums[i] < 2^31
"""
from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_counter = Counter(nums)
        for key, value in num_counter.items():
            if value == 1:
                return key
# 上面的方法虽然能通过，但肯定有其他的方法来做。


if __name__ == '__main__':
    solu = Solution()
    nums = [9,1,7,9,7,9,7]
    ans = solu.singleNumber(nums)
    print(ans)

