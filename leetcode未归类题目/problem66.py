"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
"""
# leetcode 的刷题方式都是让你写出类或者方法就可以了

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(1,len(digits)+1):
            if digits[-i] !=9:
                digits[-i] +=1
                return digits
            digits[-i]=0
        digits.insert(0,1)
        return digits

solu = Solution()
a = [1,2,3]

answer = solu.plusOne(a)
print(answer)