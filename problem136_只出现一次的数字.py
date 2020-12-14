"""
136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4
"""
from collections import Counter
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = Counter(nums)
        for k,v in dic.items():
            if v == 1:
                return k

    def singleNumber_2(self, nums: List[int]) -> int:
        # 题目要求我们应该具有O(N)时间复杂度，不使用额外空间，我上面的解法使用了计数器的功能
        # 我们发现其余每个元素都是出现两次，那么 set(list) * 2 - sum(list) = 只出现一次元素的值
        # 但是我们我感觉这里还是使用了set集合，这里应该算了额外的空间复杂度 O(N)
        sum1 = sum(nums)
        sum2 = sum(set(nums))
        result = 2 * sum2 - sum1
        return result

    def singleNumber_3(self, nums: List[int]) -> int:
        # 我看题解，还有一个位运算。对于这道题，可使用异或运算。异或运算有以下三个性质。
        # 任何数和 0 做异或运算，结果仍然是原来的数，即 a⊕0 = a。
        # 任何数和其自身做异或运算，结果是 0，即 a⊕a=0。
        # 异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。
        # 假设数组中有 2m+1个数，其中有m个数各出现两次，一个数出现一次，令a1，a2，...am为出现两次的m个数，
        # am+1为出现一次的数。根据性质3，数组中的全部元素的异或运算结果总是可以写成如下形式：
        # (a1⊕a1)⊕(a2⊕a2)⊕...⊕(am⊕am)⊕am+1 = 0⊕0⊕...⊕0⊕am+1 = am+1 这样结果就出来了哈。牛逼
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)


solu = Solution()
nums = [4,1,2,1,2]
ans = solu.singleNumber_2(nums)
print(ans)
