
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[float('inf')] * n for _ in range(n)]
        for j in range(0, n):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i][j-1])
                    else:
                        for k in range(i, j):
                            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

        # print(dp)
        return dp[0][n-1]

if __name__ == '__main__':
    solu = Solution()
    s = "aba"
    ans = solu.strangePrinter(s)
    print(ans)