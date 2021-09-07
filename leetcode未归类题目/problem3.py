"""
无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""
# 采用滑动窗口的方式来解决问题，从这次题目中也看出滑动窗口用于解决这种连续的字符串的子串问题比较好
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left = 0
        right = 0
        substr = ""
        maxans = 0
        window = Counter()
        while right < len(s):
            char = s[right]
            right += 1
            if char not in window.keys():
                window[char] = 1
            else:
                window[char] += 1

            while any(map(lambda x: window[x] > 1, window.keys())):
                window[s[left]] -= 1
                left += 1
            maxans = max(maxans, sum(map(lambda x: window[x] == 1, window.keys())))
        return maxans

solu = Solution()
s = " "
ans = solu.lengthOfLongestSubstring(s)
print(ans)






