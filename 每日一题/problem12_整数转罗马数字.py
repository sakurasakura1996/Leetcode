class Solution:
    def intToRoman(self, num: int) -> str:
        intToRomanMap = {1: 'I',
                         4: 'IV',
                         5: 'V',
                         9: 'IX',
                         10: 'X',
                         40: 'XL',
                         50: 'L',
                         90: 'XC',
                         100: 'C',
                         400: 'CD',
                         500: 'D',
                         900: 'CM',
                         1000: 'M'}
        # 给定一个数，不断倒序计算，如果满足就循环减
        ans = ""
        intToRomanMap = sorted(intToRomanMap.items(), key=lambda x:(x[0], x[1]), reverse=True)
        # print(type(intToRomanMap))  # 注意上面的排序方法会让dict变成list啊
        while num:
            for key,value in intToRomanMap:
                if num >= int(key):
                    num -= int(key)
                    ans += value
                    break
        return ans


if __name__ == '__main__':
    solu = Solution()
    ans = solu.intToRoman(1994)
    print(ans)
