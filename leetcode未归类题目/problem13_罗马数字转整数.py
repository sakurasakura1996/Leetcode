class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000,
                    'IV':4,
                    'IX':9,
                    'XL':40,
                    'XC':90,
                    'CD':400,
                    'CM':900}
        ans = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and (s[i]+s[i+1]) in num_dict:
                ans += num_dict[s[i]+s[i+1]]
                i += 2
            else:
                ans += num_dict[s[i]]
                i += 1
        return ans

if __name__ == '__main__':
    solu = Solution()
    s = "MCMXCIV"
    ans = solu.romanToInt(s)
    print(ans)
