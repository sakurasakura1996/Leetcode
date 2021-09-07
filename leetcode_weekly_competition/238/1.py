class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = []
        while n != 0:
            ans.append(n%k)
            n //= k
        print(ans)
        return sum(ans)


if __name__ == '__main__':
    solu = Solution()
    ans = solu.sumBase(10, 10)
    print(ans)