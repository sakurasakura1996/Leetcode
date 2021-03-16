"""
剑指 Offer 61. 扑克牌中的顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
示例 1:
输入: [1,2,3,4,5]
输出: True

示例 2:
输入: [0,0,1,2,5]
输出: True
限制：
数组长度为 5
数组的数取值为 [0, 13] .
"""
# 除0以外，最大值减最小值要小于5.且不能有重复值
from typing import List
from collections import Counter
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        num0 = 0
        for i in range(n):
            if nums[i] == 0:
                num0 += 1
            else:
                if nums[-1] - nums[i] >= 5:
                    return False
                else:
                    num_counter = Counter(nums[i:])
                    for value in num_counter.values():
                        if value > 1:
                            return False
        return True

    def search2(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue
            ma = max(ma, num)
            mi = min(mi, num)
            if num in repeat: return False
            repeat.add(num)
        return ma - mi < 5

if __name__ == '__main__':
    solu = Solution()
    nums = [0,0,0,2,7]
    ans = solu.isStraight(nums)
    print(ans)