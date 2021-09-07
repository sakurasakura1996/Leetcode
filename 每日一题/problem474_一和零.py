from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 我们可不可以给字符串排个序，排序的规则就是字符串中0，1的个数，越少的排在前面，这样就能让
        # 最终的子集排的越多一点。但是字符串有0和1，如果一个字符串，且m，n大小不一样，那么我们怎么
        # 做到确定的排序呢。
        # 看完题解发现是用动态规划，这道题是背包问题，只不过是两个变量，需要3维dp来解决问题。
        l = len(strs)
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(l+1)]
        for k in range(1, l+1):
            n0 = strs[k-1].count("0")
            n1 = strs[k-1].count("1")
            for i in range(m+1):
                for j in range(n+1):
                    dp[k][i][j] = dp[k-1][i][j]
                    if i - n0 >= 0 and j - n1 >= 0:
                        dp[k][i][j] = max(dp[k][i][j], dp[k-1][i-n0][j-n1]+1)
        return dp[l][m][n]

if __name__ == '__main__':
    solu = Solution()
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    ans = solu.findMaxForm(strs, m, n)
    print(ans)