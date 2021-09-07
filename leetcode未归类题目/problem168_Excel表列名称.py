class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 这里比较麻烦的是，这里满26不进位，而是满27才进位，和普通的进制转换还是有点区别。
        ans = ""
        t = columnNumber
        while t > 0:
            t -= 1
            a, b = t//26, t%26
            ans = ans +chr(b+65)  # A 的ASCII码是65，
            t = a
        return ans[::-1]


if __name__ == '__main__':
    solu = Solution()
    ans = solu.convertToTitle(701)
    print(ans)