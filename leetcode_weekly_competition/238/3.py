class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        words = ['a', 'e', 'i', 'o', 'u']
        n = len(word)
        if n < 5:
            return 0
        left = 0
        right = 0
        window = 0
        ans = 0
        start = None
        while right < n:
            if word[right] == 'a' and (start == 'a' or start is None):
                window += 1
                start = 'a'
            elif word[right] == 'e' and (start == 'a' or start == 'e'):
                window += 1
                start = 'e'
            elif word[right] == 'i' and (start == 'e' or start == 'i'):
                window += 1
                start = 'i'
            elif word[right] == 'o' and (start == 'i' or start == 'o'):
                window += 1
                start = 'o'
            elif word[right] == 'u' and (start == 'o' or start == 'u'):
                window += 1
                ans = max(ans, window)
                start = 'u'
            else:
                if word[right] == 'a':
                    window = 1
                    start = 'a'
                else:
                    window = 0
                    start = None
            right += 1
        return ans

if __name__ == '__main__':
    solu = Solution()
    word = "uuuuuuuuooooooooiiiiiiiiieeeeeeeeeaaaaaaaaaauaeiou"
    ans = solu.longestBeautifulSubstring(word)
    print(ans)




