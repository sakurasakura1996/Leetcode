"""
date：2021/1/11，
昨天想不起来如何证明可以用辗转相除法或者辗转相减法来求最小公约数了，这里来回归一下吧。
设 x = gcd(m, n) ,m > n。
if m%n == 0: n 就是m，n的最大公约数
else: m = q * n + r
那么 m / x = (q * n + r) / x = q * (n/x) + (r/x) 因为x是两者的最大公约数，所以两边都是整数，所以，r可以被x整除
r = m % n,所以我们可以把 求 m，n的最大公约数 转换为两个更小的数的最大公约数，如此下去就能找到了

最小公倍数：有一个定理，我们就不证明它了，两个数的最小公倍数 = 两数的乘积 / 两数的最大公因数
"""


def gcd(m: int, n: int) -> int:
    ans = n if m%n == 0 else gcd(n, m%n)
    return ans


def lcm(m: int, n: int) -> int:
    return int(m * n / gcd(m, n))


if __name__ == '__main__':
    m = 9
    n = 6
    gcd_num = gcd(m, n)
    lcm_num = lcm(m, n)
    print(gcd_num)
    print(lcm_num)

