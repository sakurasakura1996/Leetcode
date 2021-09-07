class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        ans = nums[0]
        for i in range(1, n):
            ans = ans ^ nums[i]
        return ans

if __name__ == '__main__':
    solu = Solution()
    n = 10
    start = 5
    ans = solu.xorOperation(n, start)
    print(ans)