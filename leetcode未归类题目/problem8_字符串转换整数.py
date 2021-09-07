class Solution:
    def myAtoi(self, s: str) -> int:
        num = 1
        number = ""
        flag = 1 # 表示还没读到数字
        s = s.strip()
        for ch in s:
            if ch == '-' and flag:
                num = -num
                flag = 0
            elif ch == '+' and flag:
                flag = 0
            elif ch.isdigit():
                flag = 0
                number += ch
            else:
                break
        if not number:
            return 0
        if num < 0:
            return num * int(number) if num * int(number) > -2**31 else -2**31
        else:
            return num * int(number) if num * int(number) < 2**31-1 else 2**31-1


if __name__ == '__main__':
    solu = Solution()
    s =  "-+12"
    ans = solu.myAtoi(s)
    print(ans)
