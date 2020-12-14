"""
438. 找到字符串中所有字母异位词
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。

示例 1:
输入:
s: "cbaebabacd" p: "abc"
输出:
[0, 6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

示例 2:
输入:
s: "abab" p: "ab"
输出:
[0, 1, 2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
"""
# 使用滑动窗口一个很好的出发点就是，改题目要求的就是连续子串。
from collections import Counter
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p_counter = Counter(p)
        if not s:
            return []
        s_len = len(s)
        p_len = len(p)
        left = 0
        right = 0
        window = Counter()
        ans = []
        while right < s_len:
            c = s[right]
            if c not in p_counter:
                window.clear()
                left = right = right + 1
            else:
                window[c] = window[c] + 1
                if right - left + 1 == p_len:
                    if window == p_counter:
                        ans.append(left)

                    window[s[left]] -= 1
                    left += 1
                right += 1
        return ans


solu = Solution()
s = "abab"
p = "ab"
ans = solu.findAnagrams(s, p)
print(ans)

