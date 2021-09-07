class Solution:
    def reverse(self, x: int) -> int:
        num = 1
        if x < 0:
            num = -1
            x = str(x)[1:]
        else:
            num = 1
            x = str(x)

        return num * int(x[::-1]) if 2**31-1 >= num * int(x[::-1]) >= -2**31 else 0


if __name__ == '__main__':
    solu = Solution()
    x = 0
    ans = solu.reverse(x)
    print(ans)
