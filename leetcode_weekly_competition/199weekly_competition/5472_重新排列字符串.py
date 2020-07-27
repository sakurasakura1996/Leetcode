"""
5472. 重新排列字符串  显示英文描述
通过的用户数 0
尝试过的用户数 0
用户总通过次数 0
用户总提交次数 0
题目难度 Easy
给你一个字符串 s 和一个 长度相同 的整数数组 indices 。

请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。

返回重新排列后的字符串。
输入：s = "codeleet", indices = [4,5,6,7,0,2,1,3]
输出："leetcode"
解释：如图所示，"codeleet" 重新排列后变为 "leetcode" 。
"""
from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a = list(s)
        n = len(indices)
        ans = []
        cter = {}
        for i in range(n):
            cter[indices[i]] = i
        for i in range(n):
            ans.append(a[cter[i]])
        return ''.join(ans)

solu = Solution()
s = "aiohn"
indices = [3,1,4,2,0]

ans = solu.restoreString(s,indices)
print(ans)
