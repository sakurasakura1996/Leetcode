class Solution:
    """
    @param s: a string.
    @return: return the values of all the intervals.
    """
    def suffixQuery(self, s):
        # write your code here
        from collections import defaultdict
        n = len(s)
        ans = 0
        for i in range(n):
            ans += 1
            left = i - 1
            right = i + 1
            while left >=0 and right < n:
                if s[left] == s[right]:
                    ans += 1
                left -= 1
                right += 1
        for i in range(n-1):
            left = i
            right = i+1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    ans += 1
                left -= 1
                right += 1
        return ans


solu = Solution()
s = "bacbdab"
ans = solu.suffixQuery(s)
print(ans)
