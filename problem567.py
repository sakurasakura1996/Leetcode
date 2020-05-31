"""
567. 字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。
示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False
"""
# 首先想到的是Counter 来记录每个字符出现的次数，然后判断是否相等
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > len(s2):
            return False
        left = 0
        right = s1_len
        while right <= s2_len:
            window = s2[left:right]
            s2_counter = Counter(window)
            if all(map(lambda x:s2_counter[x] == s1_counter[x], window)):
                return True
            else:
                s2_counter[s2[left]] -= 1
                if right < s2_len:
                    s2_counter[s2[right]] += 1
                left += 1
                right += 1
        return False

solu = Solution()
s1 = "adc"
s2 = "dcda"
ans = solu.checkInclusion(s1,s2)
print(ans)

