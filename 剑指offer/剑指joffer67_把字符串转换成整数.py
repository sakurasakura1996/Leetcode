"""

"""
class Solution:
    def strToInt(self, str: str) -> int:
        if not str:return 0
        str = str.strip()
        if str == "":return 0
        n = len(str)
        num = "0"  # 注意有坑的地方，如果字符串只是 "+"这种，就很麻烦
        ans = 0
        if str[0] == '+':
            for i in range(1,n):
                if str[i] >= '0' and str[i] <= '9':
                    num += str[i]
                else:
                    break
            ans = int(num) if int(num) <= pow(2,31) - 1 else pow(2, 31) - 1
        elif str[0] == '-':
            for i in range(1, n):
                if str[i] >= '0' and str[i] <= '9':
                    num += str[i]
                else:
                    break
            ans = -int(num) if -int(num) >= -pow(2, 31) else -pow(2, 31)
        elif str[0] >= '0' and str[0] <= '9':
            for i in range(n):
                if str[i] >= '0' and str[i] <= '9':
                    num += str[i]
                else:
                    break
            ans = int(num) if int(num) <= pow(2,31) - 1 else pow(2, 31) - 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    str = "+"
    ans = solu.strToInt(str)
    print(ans)


