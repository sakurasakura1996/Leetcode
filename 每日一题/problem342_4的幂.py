class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
        else:
            while n != 1:
                if n % 4 == 0:
                    n = n // 4
                else:
                    return False
            return True

    def isPowerOfFour2(self, n: int) -> bool:
        # 题目要求不使用循环或者递归来完成，那么其实昨天做了一道2的幂的题目，思路应该是相似的，我们需要自己推理下。
        # 之前是2的幂，现在是4的幂转换成2的整数幂，不过2的指数是偶数就满足条件了
        # 转换成二进制的话，后面0的个数是偶数个。
        if n < 1:return False
        if n == 1:return True
        if n > 1 and (n & -n) == n:
            while n != 0:
                if n == 1:
                    return True
                n = n >> 2
            return False
        else:
            return False



if __name__ == '__main__':
    solu = Solution()
    ans = solu.isPowerOfFour2(2)
    print(ans)