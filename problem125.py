"""
125.验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        # 字符串中的空格符号都给它去掉再把大写字母转成小写
        #　判断字符是否是字母　python可以用 char.isalnum()来判断
        s_change = "".join(ch.lower() for ch in s if ch.isalnum())
        return s_change == s_change[::-1]


s =  "A man, a plan, a canal: Panama"
solu = Solution()
ans = solu.isPalindrome(s)
print(ans)
