class Solution:
    """
    @param s: The given string
    @return: return the number of Five-character palindrome
    """
    def Fivecharacterpalindrome(self, s):
        # write your code here
        if not s or len(s) < 5:
            return 0
        n = len(s)
        left = 0
        right = 4
        ans = 0

        def check(l,r)->int:
            if s[left] == s[right] and s[left+1] == s[right-1] and s[left] != s[left+1] and s[left] != s[left+2] and s[left+1]!=s[left+2]:
                return 1
            else:
                return 0

        while right < n:
            ans += check(left, right)
            left += 1
            right += 1
        return ans

solu = Solution()
s = "abcbabcccb"
ans = solu.Fivecharacterpalindrome(s)
print(ans)