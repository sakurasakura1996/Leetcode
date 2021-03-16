"""
输入整数n，求1-n这n个整数的十进制表示中1出现的次数
"""
# 这道题和剑指offer第44题问的东西很相似，这种题目看着没啥技巧就很不喜欢做
class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = [0] * (n+1)
        for i in range(1, n+1):

