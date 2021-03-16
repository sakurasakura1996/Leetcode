"""
剑指 Offer 16. 数值的整数次方
实现函数double Power(double base, int exponent)，求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题。
示例 1:
输入: 2.00000, 10
输出: 1024.00000

示例 2:
输入: 2.10000, 3
输出: 9.26100

示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
注意：本题与主站 50 题相同
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        abn = abs(n)
        double = abn // 2
        single = x if abn % 2 else 1
        if double > 1:
            ans = self.myPow(x * x, double) * single
        elif double == 1:
            ans = x * x * single
        elif double == 0 and single == 1:
            ans = 1
        elif double == 0 and single == x:
            ans = single

        if n < 0:
            return 1/ans
        else:
            return ans


if __name__ == '__main__':
    solu = Solution()
    ans = solu.myPow(2.00000, -2)
    print(ans)


