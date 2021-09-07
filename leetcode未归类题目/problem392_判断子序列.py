"""
392. 判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
示例 1:
s = "abc", t = "ahbgdc"
返回 true.
示例 2:
s = "axc", t = "ahbgdc"
返回 false.
后续挑战 :
如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
"""
from collections import Counter
class Solution:
    def inSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        s_point = 0
        t_point = 0
        # 利用指针分别指向s和t
        while s_point < s_len and t_point < t_len:
            if s[s_point] == t[t_point]:
                s_point += 1
                t_point += 1
            else:
                t_point += 1
        if t_point == t_len and s_point < s_len:
            return False
        if s_point == s_len:
            return True

    def inSubsequence_2(self, s: str, t: str) -> bool:
        # 题解还给出了一种动态规划的方法来应付题目中的挑战：使用动态规划的方法来进行预处理，令dp[i][j]表示字符串t中从位置i开始往后字符j第一次出现的位置。
        # 在进行状态转移时，如果t中位置i的字符就是j，那么dp[i][j]=i，否则j出现在位置i+1开始往后，即dp[i][j]=dp[i+1][j]，因此我们要倒过来
        # 进行动态规划，从后往前枚举i。
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)
        # f[i][j] = m表示位置i开始往后不存在字符j了

        for i in range(m-1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i+1][j]

        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1

        return True


solu = Solution()
s = "abc"
t = "ahbgdc"
ans = solu.inSubsequence(s,t)
print(ans)

