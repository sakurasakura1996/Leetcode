"""
粉刷天花板
你想给自己盖栋房子。 房子是正方形或长方形的，它的长和宽需要属于集合s，并且其面积不超过a。请问有多少组可能的长宽的组合？
集合s的n个元素的计算方法如下，给定了一个种子s0，和参数k,b和m，并通过以下公式计算si
si = ((k * si-1 +b)mod m + 1 + si-1) for 1 <= i < n
1 <= n <= 6*10^6
1 <= si <= 10^9
1 <= k,b,m <= 10^9
1 <= a <= 10^18
样例 1
输入:
s_0 = 2
n = 3
k = 3
b = 3
m = 2
a = 15
输出: 5
"""
# 我们仔细观察题目里s数组生成的式子，我们可以发现s数组是递增的，即 s_i > s{i-1}恒成立。因此，我们要求满足s_i * s_j <= a的(i,j)即可
# 很显然，当s_j越来越小时，s_i的上界就越来越大。因此，我们可以使用双指针的做法来统计答案。右指针指向j，左指针指向i，随着j的减小，i越来越大

class Solution:
    """
    @param s0: the number s[0]
    @param n: the number n
    @param k: the number k
    @param b: the number b
    @param m: the number m
    @param a: area
    @return: the way can paint the ceiling
    """
    # 方法一是我自己写的，妈的一直没通过，关键还不知道是不是超时了
    def painttheCeiling(self, s0, n, k, b, m, a):
        # write your code here
        s = [0] * n
        s[0] = s0
        # s_set = set()
        # s_set.add(s0)
        for i in range(1, n):
            s[i] = ((k * s[i - 1] + b) % m + 1 + s[i - 1])
            # s_set.add(s[i])
        ans = 0
        s.sort()

        # 应该是下面的复杂度过高，题目也说了暴力不适合大数据
        for i in range(n):
            for j in range(n):
                if s[i] * s[j] <= a:
                    ans += 1
                else:
                    break
        return ans

    def painttheCeiling_2(self, s0, n, k, b, m, a):
        # write your code here
        ans = 0
        right = n - 1
        s = []
        s.append(s0)
        last = s0
        for i in range(1, n):
            last = (k * last + b)%m + 1 + last
            s.append(last)
        for i in range(n):
            while (right >= 0 and s[right] * s[i] > a):
                right -= 1
            ans += right + 1
        return ans



s_0 = 2
n = 3
k = 3
b = 3
m = 2
a = 15
solu = Solution()
ans = solu.painttheCeiling(s_0,n,k,b,m,a)
print(ans)
