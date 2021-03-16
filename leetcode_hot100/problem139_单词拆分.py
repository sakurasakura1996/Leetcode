"""
139. 单词拆分
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
from collections import defaultdict
from functools import lru_cache
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 代码写的是真的丑，这个方法应该是已经可行了，只不过超时了，其实用的就是暴力法。难怪会超时
        word_dict = defaultdict(list)
        for word in wordDict:
            w = word[0]
            word_dict[w].append(word)

        def check(s, l, word_dict: defaultdict) -> bool:
            if not s or l == 0:
                return True
            start = s[0]
            if not word_dict[start]:
                return False
            else:
                flag = False
                for word in word_dict[start]:
                    if len(word) <= l and s[:len(word)] == word:
                        flag = True and check(s[len(word):], l-len(word), word_dict)
                        if flag:
                            return flag

                return flag

        ans = check(s, len(s), word_dict)
        return ans

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        # 这道题没想到可以用动态规划是不要应该的啊，应该说，如果想到了动态规划这个念头，那你就应该去想想动态规划是否可行啊，不要不动脑子啊
        if not s:return True
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
        # 这里写了两种，我自己应该是更倾向于前者的写法
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         if (dp[i] and (s[i:j] in wordDict)):
        #             dp[j] = True
        return dp[n]

    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        # 我第一个写的其实就是暴力回溯，超时了，题解中有一个记忆化回溯，值得学习一下哈,保存出现过的 backtrace(s)，避免出现重复计算

        @lru_cache(None)
        def backtrace(s):
            if not s:
                return True
            ans = False
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    ans = backtrace(s[i:]) or ans
            return ans
        return backtrace(s)



if __name__ == '__main__':
    solu = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    ans = solu.wordBreak2(s, wordDict)
    print(ans)

