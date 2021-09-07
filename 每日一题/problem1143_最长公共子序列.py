class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        # 初始化都为0，不用初始化了
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                flag = 1 if text1[i-1] == text2[j-1] else 0
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+flag)
        return dp[n1][n2]


if __name__ == '__main__':
    solu = Solution()
    text1 = "abc"
    text2 = "def"
    ans = solu.longestCommonSubsequence(text1, text2)
    print(ans)