class Solution:
    def countSubstrings(self, s: str) -> int:
        # 准备用中心扩展的思路，因为一个字符串长度为奇数时，它肯定有一个中心字符，为偶数时，中心就是中间两个字符，我们遍历一遍，然后不断像两边扩展
        n = len(s)
        if n == 0 or n == 1:
            return n
        ans = 0
        for i in range(n):
            left = right = i
            while left >= 0 and right <= n-1:
                if s[left] == s[right]:
                    ans += 1
                    left -= 1
                    right += 1
                else:
                    break

        for i in range(n-1):
            left, right = i, i+1
            while left >=0 and right <= n-1:
                if s[left] == s[right]:
                    ans += 1
                    left -= 1
                    right += 1
                else:
                    break
        return ans


if __name__ == '__main__':
    solu = Solution()
    s = "aaa"
    ans = solu.countSubstrings(s)
    print(ans)