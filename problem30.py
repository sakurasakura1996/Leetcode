"""
30. 串联所有单词的子串
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：
输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

最开始想到的是暴力法，但是做这题时已经知道可以用滑动窗口法来做，所以就在想，感觉暴力法和滑动窗口的想法很相似了，我最初的想法是
找到words中每个单词在s中的起始位置，那么只需要从这些起始位置开始检测是否可以满足要求。这样的话，不用遍历s中的每一个字符。但是
感觉还不算快，后续再看看题解吧。滑动窗口是怎么做的.好蠢啊，滑动窗口经常会用到 Counter啊
"""
from collections import Counter
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        words_len = len(words)
        n = len(s)
        words = Counter(words)
        ans = []
        for i in range(word_len):
            cur_cnt = 0
            left = i
            right = i
            cur_counter = Counter()
            while right + word_len <= n:
                w = s[right:right+word_len]
                right += word_len
                cur_counter[w] += 1
                cur_cnt += 1
                while cur_counter[w] > words[w]:
                    # left 右移
                    left_w = s[left:left+word_len]
                    left += word_len
                    cur_counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == words_len:
                    ans.append(left)
        return ans




solu = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
ans = solu.findSubstring(s, words)
print(ans)

