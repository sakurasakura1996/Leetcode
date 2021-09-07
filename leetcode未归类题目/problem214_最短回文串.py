"""
214. 最短回文串
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
示例 1:
输入: "aacecaaa"
输出: "aaacecaaa"

示例 2:
输入: "abcd"
输出: "dcbabcd"
"""
# 这题目前看上去倒没有那么难，但是问题难度是hard，我想到的是，能够缩短回文串长度的原因就只有，现在的字符串 s
# 从s[0]到 s[i]已经是回文的了，然后我只需要在字符串的前面补上s[i+1]到s[-1]部分字符串的倒置即可。
# 那么现在问题就回到了如何查找字符串s前面的回文串。是否可以用双指针，
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # 感觉自己的解法大概率超时
        def huiwen(s, j):
            # 判断字符串s从s[0]到s[j]是否回文
            left = 0
            right = j
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
                    break
            return True
        n = len(s)
        right_point = n-1
        maxj = 0
        for i in range(n-1, -1, -1):
            if huiwen(s, i):
                maxj = max(maxj, i)

        # 那么就代表s内部有一部分是回文串了。
        subStr = ''.join(reversed(s[maxj+1:]))

        return subStr + s

    def shortestPalindrome(self, s: str) -> str:
        # 思路是对的了，但是关键问题在s字符串，如何找到它的最长前缀回文子串呢，我上面就是枚举暴力，太慢了
        # 看题解中提到要求最长回文前缀，用什么回文大杀器  Manacher算法或者KMP算法，我晕了啊。然后看到一个几行代码的暴力法竟然过了
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s
        # 这也太牛逼了吧，主要还是使用了自己不熟悉的函数 startswith，然后这里的暴力法可以这样思考，我打算把整个s倒置加到s前面，这时候
        # 如何减少长度呢，那就是看倒置的s和s总共最长重合了多长的子串。

    def shortestPalindrome(self, s: str) -> str:
        # 上面暴力法的大佬还有一个递归方法，学习学习,为什么别人写的代码都这么简洁而且快啊。
        j = 0
        # 找到从头开始，最长的回文子串
        for i in range(len(s) - 1, -1, -1):
            if s[i] == s[j]:
                j+=1
        if j==len(s):
            return s
        # 后缀
        suffix = s[j:]
        return suffix[::-1] + self.shortestPalindrome(s[:j]) + suffix






solu = Solution()
s = "abcd"
ans = solu.shortestPalindrome(s)
print(ans)