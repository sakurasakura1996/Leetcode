"""
5562. 字符频次唯一的最小删除次数
如果字符串 s 中 不存在 两个不同字符 频次 相同的情况，就称 s 是 优质字符串 。
给你一个字符串 s，返回使 s 成为 优质字符串 需要删除的 最小 字符数。
字符串中字符的 频次 是该字符在字符串中的出现次数。例如，在字符串 "aab" 中，'a' 的频次是 2，而 'b' 的频次是 1 。
"""
from collections import Counter
class Solution:
    def minDeletions(self, s:str) -> int:
        s_counter = Counter(s)
        a = set()
        counter = list()
        b = set()
        for key, value in s_counter.items():
            a.add(value)
            counter.append(value)

        counter.sort(reverse=True)
        ans = 0
        for i, num in enumerate(counter):
            if num not in b:
                b.add(num)
            else:
                cur = num
                while cur in a or cur in b:
                    cur -= 1
                    ans += 1
                if cur != 0:
                    b.add(cur)
        return ans


solu = Solution()
s = "bbcebab"
ans = solu.minDeletions(s)
print(ans)

