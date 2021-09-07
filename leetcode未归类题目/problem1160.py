"""
拼写单词
给你一份词汇表（字符串数组）words 和一张字母表（字符串）chars
假如你可以用chars中的字母（字符）拼写出words中的某个单词（字符串）那么我们就认为你掌握了
这个单词
注意：每次拼写词汇表中的一个单词时，chars中的每个字母都只能用一次
返回词汇表words中你掌握的所有单词的长度之和
"""
from typing import List
import collections
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            chars_list = [char for char in chars]
            flag = 1

            for char in word:
                if char in chars_list:
                    chars_list.remove(char)
                else:
                    flag = 0
                    break
            if flag:
                ans += len(word)
        return ans
"""
这是一类经典的题型。凡是和“变位词”、“字母顺序打乱”相关的题目，都考虑统计字母出现的次数。这种方法我叫做 “counter 方法”，因为 Python 中有个 
Counter 类就是专门用来计数的。
显然，对于一个单词 word，只要其中的每个字母的数量都不大于 chars 中对应的字母的数量，那么就可以用 chars 中的字母拼写出 word。所以我们只需要
用一个哈希表存储 chars 中每个字母的数量，再用一个哈希表存储 word 中每个字母的数量，最后将这两个哈希表的键值对逐一进行比较即可。

"""
class Solution2:
    def solve(self,words: List[str], chars: str)-> int:
        ans = 0
        chars_cnt = collections.Counter(chars)    # 学会使用这种 python提供的类
        for word in words:
            word_cnt = collections.Counter(word)
            for c in word_cnt:
                if chars_cnt[c] < word_cnt[c]:
                    break
            else:  # 大意是说当迭代的对象迭代完并为空时，位于else的子句将执行，而如果在for循环中含有break时则直接终止循环，并不会执行else子句。
                # 注意这里的else的使用方法哦，这样写的话会更加简洁，以前一般用一个flag来判定，过于烦琐了。
                ans += len(word)
        return ans


solu = Solution2()
words = ["cat", "bt", "hat", "tree"]
chars = "atach"
ans = solu.solve(words,chars)
print(ans)


