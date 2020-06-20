"""
14.最长公共前缀
编写函数来查找字符串数组中的最长公共前缀
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
"""
# from typing import List
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         if len(strs) == 1 or strs[0] == "":
#             return strs[0]
#         for i in range(len(strs[0])):
#             for j in range(1,len(strs)):
#                 if len(strs[j])-1 < i or strs[j][i] != strs[0][i]:
#                     return strs[0][:i]
#         return strs[0]

# 这题目虽然不难，困难程度为简单，但是还是提交了很多次才通过，可以关注关注的
# 看了题解，觉得题解中的方法一还是应该要想出来的，这才是解决这道题最常规最不错的方法
# 那就是想想，从头开始第一个字符串和第二个字符串进行对比，找到两个字符串之间的最长公共前缀，那么再把这个前缀拿去和第三个字符串比对，因为后面的
# 最长公共前缀肯定是等于或者短于前面的公共前缀的。
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1 or strs[0] == "":
            return strs[0]
        ans = strs[0]
        idx = 1
        while idx < len(strs):
            for i in range(min(len(ans), len(strs[idx]))):
                if strs[idx][i] != ans[i]:
                    ans = ans[:i]
                    break
            ans = ans[:min(len(ans), len(strs[idx]))]
            idx += 1

        return ans


solu = Solution()
# strs = ["flower","flow","flight"]
# strs = ["c", "c"]
strs = ["aa", "a"]
ans = solu.longestCommonPrefix(strs)
print(ans)