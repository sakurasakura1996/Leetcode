"""

"""
# 用动态规划试试吧
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]


if __name__ == '__main__':
    solu = Solution()
    s = "bbbab"
    ans = solu.longestPalindromeSubseq(s)
    print(ans)


