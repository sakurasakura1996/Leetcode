"""
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
限制：
1 <= s 的长度 <= 8
"""
# 准备用回溯方法来做
from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = set()
        n = len(s)

        def backtrack(a: List[str], b:str):
            # 记住回溯的模板，已选择列表，可选择的列表
            if len(b) == n and b not in ans:
                ans.add(b)
                return
            for i, num in enumerate(a):
                b += num
                a_copy = a.copy()
                a = a[:i] + a[i+1:]
                backtrack(a, b)
                a = a_copy
                b = b[:-1]

        a = []
        for i in range(n):
            a.append(s[i])
        b = ""
        backtrack(a, b)
        return list(ans)

    def permutation2(self, s: str) -> List[str]:

if __name__ == '__main__':
    solu = Solution()
    s = "abc"
    ans = solu.permutation(s)
    print(ans)


