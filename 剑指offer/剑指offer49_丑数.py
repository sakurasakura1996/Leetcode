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
# 这题我有点印象，可以搞三个指针，不断往后排
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2 = 0
        p3 = 0
        p5 = 0
        ans = [1]
        while len(ans) < n:
            min_num = min(ans[p2]*2, ans[p3]*3, ans[p5]*5)
            ans.append(min_num)
            if min_num == ans[p2] * 2:
                p2 += 1
            if min_num == ans[p3] * 3:
                p3 += 1
            if min_num == ans[p5] * 5:
                p5 += 1
        return ans[-1]


if __name__ == '__main__':
    solu = Solution()
    n = 10
    ans = solu.nthUglyNumber(n)
    print(ans)


