class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 此种暴力方法肯定超时啊，因为参数中的两个字符串长度最大可以到四次方，乘起来就是8次方了。
        if not needle:
            return 0
        n1 = len(haystack)
        n2 = len(needle)
        for i in range(n1):
            start = i
            n = 0
            while start < n1 and n < n2 and haystack[start] == needle[n]:
                start += 1
                n += 1
            if n == n2:
                return i
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n1 = len(haystack)
        n2 = len(needle)
        if n2 > n1:
            return -1
        for i in range(n1 - n2 + 1):
            if haystack[i:i+n2] == needle:
                return i
        return -1


if __name__ == '__main__':
    solu = Solution()
    haystack = "hwwlo"
    needle = "wl"
    ans = solu.strStr2(haystack, needle)
    print(ans)