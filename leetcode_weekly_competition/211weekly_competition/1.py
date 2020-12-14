class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return -1
        ans = -1
        for i in range(n-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    ans = max(ans, j-i-1)
        return ans

solu = Solution()
s = "cabbac"
ans = solu.maxLengthBetweenEqualCharacters(s)
print(ans)
