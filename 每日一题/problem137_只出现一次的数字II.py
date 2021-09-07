from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        for key, value in nums_counter.items():
            if value == 1:
                return key

# 简单方法就能实现，但是非要用O（1）空间复杂度来完成的话，好像是要记录每位1出现的次数，然后取余，因为其他数出现的次数都是3的倍数
    def singleNumber2(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans
