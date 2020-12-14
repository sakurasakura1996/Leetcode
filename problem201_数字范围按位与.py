""""
201. 数字范围按位与
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1:

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0
"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 大概率超时，因为这是暴力法
        if m == n:return m
        ans = m
        for i in range(m+1, n+1):
            ans = ans & i
        return ans

    def rangeBitwiseAnd_2(self, m: int, n: int) -> int:
        # 猜想应该是有什么规律可以减少运算。哎，还是没想到，按位与有一个性质啊，只要
        # 对应位置有0，那么不管怎么按位与，这一位肯定都是0，那么多个数按位相与的时候，
        # 那么就是这么多数的公共前缀不变，然后后面全部补0。
        # 那么问题变成了求m 和n 的公共前缀，然后后面全部补0
        shift = 0
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift




solu = Solution()
ans = solu.rangeBitwiseAnd(5, 7)
print(ans)
