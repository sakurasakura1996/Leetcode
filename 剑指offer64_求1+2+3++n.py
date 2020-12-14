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
# 因为不能使用if判断语句，我们可以使用逻辑运算符的短路效应来代替判断语句。
class Solution:
    ans = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n-1)
        self.ans += n
        return self.ans

if __name__ == '__main__':
    solu = Solution()
    ans = solu.sumNums(3)
    print(ans)

