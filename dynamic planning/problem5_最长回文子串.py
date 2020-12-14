"""
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 不是官方题解竟然都超时了，我吐了
        n = len(s)
        if n < 2:
            return s
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l + 1
        for l in range(n):
            # 枚举子串的起始位置，
            for i in range(n):
                j = i + l
                if j >= n:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and l+1 > len(ans):
                    ans = s[i:j+1]
        return ans

    def longestPalindrome_2(self, s: str) -> str:
        # 这个注意常用写法不对奥，baby，分析出来原因在于，我的递推公式
        # dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j]) 这里的dp[i+1][j-1]还没算呢，那肯定不对了啊
        # 修改了之后还是超时啊。
        n = len(s)
        if n < 2:
            return s
        dp = [[False] * n for _ in range(n)]
        ans = s[0]
        # for i in range(n):
        #     dp[i][i] = True
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if j-i == 0:
                    dp[i][j] = True
                elif j-i == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and len(ans) < (j-i+1):
                    ans = s[i:j+1]
        return ans

solu = Solution()
s = "cccc"
ans = solu.longestPalindrome_2(s)
print(ans)