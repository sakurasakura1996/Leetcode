"""
最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
# way1
# from collections import Counter
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         window = Counter()
#         if len(s) == 0 or len(s) == 1:
#             return len(s)
#         left = 0
#         right = 0
#         mini_str = []
#         ans = 0
#         while right < len(s):
#             window[s[right]] += 1
#             mini_str.append(s[right])
# # 下面代码中的while判断感觉一直不是很好，因为any的话就是要判断 len(mini_str)次条件，会增加时间复杂度
#             while any(map(lambda x: window[x] > 1, mini_str )):
#                 window[s[left]] -= 1
#                 mini_str.pop(0)
#                 left += 1
#             # ans = max(ans, len(window))   # 这里不能用 len(window)  这种'p':0这种也会被算入长度中，
#             ans = max(ans,len(mini_str))
#             right += 1
#         return ans


# way2 思路二：优化的滑动窗口（哈希表）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        n = len(s)
        # 这里用的不是Counter（counter用于记录key值的次数，而这里需要的是记录每个key出现在字符串中的位置，索引）
        hashmap = {}

        for right in range(n):
            if s[right] in hashmap:
                left = hashmap[s[right]]
            hashmap[s[right]] = right + 1
            ans = max(ans, right-left+1)
        return ans




s = "pwwkew"
solu = Solution()
ans = solu.lengthOfLongestSubstring(s)
print(ans)
