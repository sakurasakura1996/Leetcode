"""
647. 回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
提示：
输入的字符串长度不会超过 1000 。
"""
class Solution:
    def countSubstrings(self, s:str) -> int:
        # 通常这种暴力解法都会超时，呜呜呜
        if not s:
            return 0
        n = len(s)
        ans = 0

        def check(l,r):
            left, right = l, r
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        for i in range(n):
            for j in range(i,n):
                if check(i,j):
                    ans += 1
        return ans

    def countSubstrings_2(self, s: str) -> int:
        # 上面这种枚举所有子串然后判断是否回文的做法，光枚举都已经O(N^2)了，所以还有一种就是我们从最简单的回文子串然后向外扩展计算
        def check(l,r):
            num = 0
            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                num += 1
                l -= 1
                r += 1
            return num

        if not s:
            return 0
        n = len(s)
        ans = 0
        for i in range(n):
            ans += check(i,i)
            ans += check(i,i+1)
        return ans



solu = Solution()
s = "abc"
ans = solu.countSubstrings_2(s)
print(ans)

