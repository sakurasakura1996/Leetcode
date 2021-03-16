"""
剑指 Offer 62. 圆圈中最后剩下的数字
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
示例 1：
输入: n = 5, m = 3
输出: 3

示例 2：
输入: n = 10, m = 17
输出: 2
限制：
1 <= n <= 10^5
1 <= m <= 10^6
"""
# 想采用链表的方式来做,但是这个m的范围也有点大啊，时间复杂度太高了。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        i = 0
        ans = list(range(n))
        while len(ans) > 1:
            i = (i + m - 1) % len(ans)
            ans.pop(i)
        return ans[0]

    def lastRemaining2(self, n: int, m: int) -> int:

        import sys
        sys.setrecursionlimit(100000)  # python手动设置递归深度，默认深度不够深

        def f(n, m):
            if n == 0:
                return 0
            x = f(n-1, m)
            return (m + x) % n

        return f(n, m)
    

if __name__ == '__main__':
    solu = Solution()
    ans = solu.lastRemaining(10, 17)
    print(ans)




