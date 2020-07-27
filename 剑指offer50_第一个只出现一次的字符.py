"""
剑指 Offer 50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
示例:
s = "abaccdeff"
返回 "b"
s = ""
返回 " "
限制：
0 <= s 的长度 <= 50000
"""
from collections import Counter
class Solution:
    def firstUniqChar(self, s:str) -> str:
        if not s:
            return " "
        s_counter = Counter(s)
        print(s_counter)

        for key in s_counter.keys():
            if s_counter[key] == 1:
                return key
        return " "

solu = Solution()
s = "abaccdeff"
ans = solu.firstUniqChar(s)
print(ans)