class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(haystack)
        for i in range(n - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

if __name__ == '__main__':
    solu = Solution()
    haystack = "aaaaa"
    needle = "bba"
    ans = solu.strStr(haystack, needle)
    print(ans)
