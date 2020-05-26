"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
"""
from collections import Counter
from typing import List
class solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        ans = ""
        left = 0
        right = 0
        minans = len(s)
        while right < len(s):
            char = s[right]
            right += 1
            if char not in window.keys():
                window[char] = 1
            else:
                window[char] += 1
            while all(map(lambda x: window[x]>=need[x],need.keys())):
                if right - left <= minans:
                    ans = s[left:right]
                    minans = right - left
                window[s[left]] -= 1
                left += 1
        return ans








a = solution()
S = "a"
T = "a"
ans = a.minWindow(S, T)
print(ans)