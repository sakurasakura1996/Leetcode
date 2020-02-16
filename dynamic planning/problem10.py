"""
正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
"""
# 开始看题目中的示例，把我给搞晕了，这里所说的正则表达式匹配，是s这个字符串可以在p中找到重复的部分，也就是p中能找到s就行了。
# 这道题缓一看不知道和动态规划有什么关系，属于困难程度的题目。呜呜呜 还是联想以下动态规划的几个步骤看看有没有思路


# way 1 递归求解，此方法是看别人题解得知的，高级
# class Solution:
#     def isMatch(self,s: str, p: str) -> bool:
#         if not p:
#             return not s
#         first_match = s and p[0] in {s[0], '.'}
#         # 如果p第二个字母是*
#         if len(p) >=2 and p[1] == '*':
#             return self.isMatch(s,p[2:]) or first_match and self.isMatch(s[1:],p)
#         else:
#             return first_match and self.isMatch(s[1:],p[1:])


# way 2 动态规划
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 边界条件，考虑 s 或 p 分别为空的情况
        if not p: return not s
        if not s and len(p) == 1: return False

        m, n = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        # 初始状态
        dp[0][0] = True
        dp[0][1] = False

        for c in range(2, n):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]

        for r in range(1, m):
            i = r - 1
            for c in range(1, n):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':  # ‘*’前面的字符匹配s[i] 或者为'.'
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:  # ‘*’匹配了0次前面的字符
                        dp[r][c] = dp[r][c - 2]
                else:
                    dp[r][c] = False
        return dp[m - 1][n - 1]



s = "ab"
p = ".*"
solu = Solution()
ans = solu.isMatch(s,p)
print(ans)


