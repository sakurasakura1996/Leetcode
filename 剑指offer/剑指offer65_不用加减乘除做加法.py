"""
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
示例:
输入: a = 1, b = 1
输出: 2
提示：
a, b 均可能是负数或 0
结果不会溢出 32 位整数
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 这道题目可以自己记忆记忆，这类题目，我们要首先想到可以是位运算啊，异或，与这类问题。
#
class Solution:
    def add(self, a: int, b: int) -> int:
        # 这样写是错误的，因为我先赋予a值变化值，结果后面b的计算又用到了a值，这里有问题啊。
        x = 0xffffffff
        a = a & x
        b = b & x
        # 我们指定b为进位结果，因为非进位 + 进位 还是用到了加法，所以需要循环计算，循环跳出的条件就是进位为0了
        while b != 0:
            a = a ^ b
            b = (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

    def add2(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b:
            a, b = a ^ b, (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

if __name__ == '__main__':
    solu = Solution()
    a = 1
    b = 1
    ans = solu.add2(a, b)
    print(ans)
