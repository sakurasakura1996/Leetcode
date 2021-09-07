"""
336. 回文对
给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

示例 1:

输入: ["abcd","dcba","lls","s","sssll"]
输出: [[0,1],[1,0],[3,2],[2,4]]
解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2:

输入: ["bat","tab","cat"]
输出: [[0,1],[1,0]]
解释: 可拼接成的回文串为 ["battab","tabbat"]
"""
# 如果用暴力法的话，首先遍历每种组合匹配都要n^2的复杂度，其次每次匹配都要判断是否是回文，判断回文还需要复杂度
# 所以该方法有点慢，不知道会不会超时，目前还没想到其他简便方法
from typing import List
class Solution:
    # 不出所料，这种解法肯定超时啊，时间复杂度太高了。
    def palindrom(self,word: str) -> bool:
            # judge if 回文
        n = len(word)
        left, right = 0, n-1
        while left <= right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                word = words[i]+words[j]
                if self.palindrom(word):
                    ans.append([i, j])
        return ans

from collections import defaultdict
class Solution2:
    # 还是超时了，哎
    def palindrom(self,word: str) -> bool:
        n = len(word)
        left, right = 0, n-1
        while left <= right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # 想到的一个解法就是，我们可以进行剪枝，不必要的匹配全部过滤掉，注意到，回文对的规律有，首先这两对的头尾字母相同
        # 那我们能不能按照顺序把这个大的数组按照首字母从a到z分开呢，这样可以减少复杂度应该
        # 只要首字母或者尾字母为a，都把该字符放入以a开头的数组中
        dic = defaultdict(list)
        n = len(words)
        nullstr = []
        for i in range(n):
            if words[i] == "":
                nullstr = [(i, words[i])]
            else:
                head_char = words[i][0]
                tail_char = words[i][-1]
                dic[head_char].append((i,words[i]))
                if head_char != tail_char:
                    dic[tail_char].append((i,words[i]))

        # 预处理，然后就分别对其中的数组进行寻找
        ans = []

        for str_list in dic.values():
            m = len(str_list)
            for i in range(m):
                for j in range(m):
                    if i == j:
                        continue
                    word = str_list[i][1] + str_list[j][1]
                    if self.palindrom(word) and [str_list[i][0], str_list[j][0]] not in ans:
                        ans.append([str_list[i][0], str_list[j][0]])
        if nullstr:
            idx = nullstr[0][0]
            for i in range(n):
                if self.palindrom(words[i]) and words[i] != "":
                    ans.append([idx, i])
                    ans.append([i, idx])
        return ans


# 注意特殊情况，有""的字符串，那么就是判断任意一个单字符串是否是回文字符串了，而且可以产生两组答案
solu = Solution2()
# words = ["abcd", "dcba", "lls", "s", "sssll"]
words = ["a","abc","aba",""]
ans = solu.palindromePairs(words)
print(ans)

"""
假设存在两个字符串s1和s2，s1+s2是一个回文串，记这两个字符串的长度分别为 len1和len2
我们分三种情况进行讨论：
1.len1 = len2,这种情况下s1是s2的翻转
2.len1 > len2,这种情况下我们可以将s1拆成左右两部分：t1 和 t2，其中t1是s2的翻转，t2是一个回文串
3.len1 < len2,这种情况下我们可以将s2拆成左右两部分，t1 和 t2，其中t2是s1的翻转，t1是一个回文串

这样，对于每一个字符串，我们令其为s1和s2中较长的那一个，然后找到可能和它构成回文串的字符串即可。

具体地说，我们枚举每一个字符串 k，令其为s1 和 s2中较长的那一个，那么 k 可以被拆分为两部分t1和t2
1.当t1是回文串时，符合情况 3，我们只需要查询给定的字符串序列中是否包含 t2 的翻转。
2.当t2是回文串时，符合情况 2，我们只需要查询给定的字符串序列中是否包含 t1 的翻转。
也就是说，我们要枚举字符串 k 的每一个前缀和后缀，判断其是否为回文串。如果是回文串，我们就查询其剩余部分的翻转是否在给定的字符串序列中出现即可。

注意到空串也是回文串，所以我们可以将 k 拆解为 k+∅ 或 ∅+k，这样我们就能将情况 1 也解释为特殊的情况 2 或情况 3。

而要实现这些操作，我们只需要设计一个能够在一系列字符串中查询「某个字符串的子串的翻转」是否存在的数据结构，有两种实现方法：

我们可以使用字典树存储所有的字符串。在进行查询时，我们将待查询串的子串逆序地在字典树上进行遍历，即可判断其是否存在。

我们可以使用哈希表存储所有字符串的翻转串。在进行查询时，我们判断带查询串的子串是否在哈希表中出现，就等价于判断了其翻转是否存在。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/palindrome-pairs/solution/hui-wen-dui-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def findWord(s: str, left: int, right: int) -> int:
            return indices.get(s[left:right + 1], -1)

        def isPalindrome(s: str, left: int, right: int) -> bool:
            return (sub := s[left:right+1]) == sub[::-1]

        n = len(words)
        indices = {word[::-1]: i for i, word in enumerate(words)}

        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])

        return ret

# 上面这个代码太难读懂了，下面这个写的比较好看
# 大多题解思路都是比较两个字符串的长度，然后来对应的匹配进行剪枝
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        list = []
        lenw = len(words)
        for i, w in enumerate(words):
            for j in range(i + 1,lenw):
                len1 = len(w)
                len2 = len(words[j])
                if len1 == len2:
                    if w == words[j][::-1]:
                        list.append([i,j])
                        list.append([j,i])
                elif len1 > len2:
                    if words[j][::-1] in w:
                        if (w + words[j]) == (w + words[j])[::-1]:
                            list.append([i,j])
                        if (words[j] + w) == (words[j] + w)[::-1]:
                            list.append([j,i])
                else:
                    if w[::-1] in words[j]:
                        if (w + words[j]) == (w + words[j])[::-1]:
                            list.append([i,j])
                        if (words[j] + w) == (words[j] + w)[::-1]:
                            list.append([j,i])
        return list
