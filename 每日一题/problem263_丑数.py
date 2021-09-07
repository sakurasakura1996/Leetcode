class Solution:
    # 注意n取值范围啊，n=0的时候要注意
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return self.isUgly(n//2)
        if n % 3 == 0:
            return self.isUgly(n//3)
        if n % 5 == 0:
            return self.isUgly(n//5)
        return False


if __name__ == '__main__':
    solu = Solution()
    ans = solu.isUgly(14)
    print(ans)