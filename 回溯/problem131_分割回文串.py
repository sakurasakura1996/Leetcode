"""
131. 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
示例:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def isHuiWen(string):
            left = 0
            right = len(string) - 1
            while left <= right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrace(s1: List[str], s2: str, length):
            if length == n:
                ans.append(s1.copy())
                return

            for i in range(1, len(s2)+1):
                if isHuiWen(s2[:i]):
                    s1.append(s2[:i])
                    backtrace(s1, s2[i:], length+i)
                    s1.pop()  # 这里不能是s1.remove(s2[:i]),因为s1中可能有多个重复的，这样remove就是去掉前面那个了。

        backtrace([], s, 0)
        return ans


if __name__ == '__main__':
    solu = Solution()
    ans = solu.partition("cbbbcc")
    print(ans)



