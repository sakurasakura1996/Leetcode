"""
剑指 Offer 49. 丑数
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
示例:
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:
1 是丑数。
n 不超过1690。
注意：本题与主站 264 题相同
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:return 1
        ans = [1]
        p2, p3, p5 =0, 0, 0
        for i in range(1, n):
            tmp2 = ans[p2] * 2
            tmp3 = ans[p3] * 3
            tmp5 = ans[p5] * 5
            min_tmp = min(tmp2, tmp3, tmp5)
            ans.append(min_tmp)
            if tmp2 == min_tmp:
                p2 += 1
            if tmp3 == min_tmp:
                p3 += 1
            if tmp5 == min_tmp:
                p5 += 1
        return ans[n-1]

if __name__ == '__main__':
    solu = Solution()
    n = 10
    ans = solu.nthUglyNumber(n)
    print(ans)
