"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

示例 3：
输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"
提示：
1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成
"""
# 第一直觉，想到的是动态规划方法来写。
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        dp = [[False] * n for _ in range(n)]
        # 时刻记录最优结果
        length = 1
        ans = s[0]

        # 初始化边界结果，dp数组只赋值上半部分，即，dp[i][j]，j>=i
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                length = 2
                ans = s[i] + s[i+1]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if j - i < 2:
                    continue
                if s[j] == s[i]:
                    dp[i][j] = dp[i+1][j-1]
                    if dp[i][j] and (j - i + 1) > length:
                        length = j - i + 1
                        ans = s[i:j+1]
        return ans

    def longestPalindrome2(self, s: str) -> str:
        # 是不是有种叫中心扩展的方法, 确实思路挺好的，思考过程不复杂，但是我下面自己写的代码不是很简洁，很冗杂
        n = len(s)
        if n == 1:
            return s
        length = 1
        ans = s[0]
        for i in range(n):
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                if right - left - 1 > length:
                    length = right - left - 1
                    ans = s[left+1:right]

        for i in range(1, n):
            left, right = i-1, i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                if right - left - 1 > length:
                    length = right - left - 1
                    ans = s[left+1:right]
        return ans


if __name__ == '__main__':
     solu = Solution()
     s = "aaabbbb"
     ans = solu.longestPalindrome(s)
     print(ans)



