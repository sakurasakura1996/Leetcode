"""
剑指 Offer 64. 求1+2+…+n
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
示例 1：
输入: n = 3
输出: 6

示例 2：
输入: n = 9
输出: 45
限制：
1 <= n <= 10000
"""
# 这种题目你要想到的是要不是位运算，要不是逻辑运算符的操作。
# 这里是通过逻辑运算符实现短路效应，不用if判断语句也能控制递归部分的实现

class Solution:
    ans = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n-1)
        self.ans += n
        return self.ans

    def sumNums2(self, n: int) -> int:
        n < 1 or self.sumNums2(n-1)
        self.ans += n
        return self.ans
