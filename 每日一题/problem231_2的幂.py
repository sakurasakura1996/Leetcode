class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n = n//2
            else:
                return False
        return True
    def isPowerOfTwo2(self, n: int) -> bool:
        # 题目要求我们不要使用循环和递归，题解中使用位运算，感觉我还是写不出来位运算的解法，妈的
        # 一个数 n 是 2 的幂，当且仅当 n 是正整数，并且 n 的二进制表示中仅包含 1 个 1。
        return n > 0 and (n & (n-1)) == 0

    def isPowerOfTwo3(self, n: int) -> bool:
        return n > 0 and (n & -n) == n


if __name__ == '__main__':
    solu = Solution()
    ans = solu.isPowerOfTwo(5)
    print(ans)