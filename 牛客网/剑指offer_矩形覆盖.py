"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法：
示例1
输入
4
返回值
5
"""
# 这道题我竟然搞不出来，发现是有规律的，竟然还可以通过动态规划来写，我真的是。。。
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, n):
        # write code here
        if n < 3:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
