class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 要求时间复杂度为O(logN),我们只需要找每个累乘的数有多少个 5 的因子即可，但是要注意，25这种有两个5的因子，所以每次遇到这种我们先除以5，
        # 用来更新 n。
        return 0 if n < 5 else n//5 + self.trailingZeroes(n//5)


if __name__ == '__main__':
    solu = Solution()
    ans = solu.trailingZeroes(10)
    print(ans)