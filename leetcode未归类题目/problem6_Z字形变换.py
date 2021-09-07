
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        n = len(s)
        if n <= numRows or numRows == 1:
            return s
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                start = i
                while start < n:
                    ans += s[start]
                    start += (2 * numRows - 2)
            else:
                interval = [(numRows - i -1) * 2, i*2]
                start = i
                flag = 1
                while start < n:
                    ans += s[start]
                    flag = (flag + 1)%2
                    start += interval[flag]
        return ans


if __name__ == '__main__':
    solu = Solution()
    s = "AB"
    numRows = 1
    ans = solu.convert(s, numRows)
    print(ans)


