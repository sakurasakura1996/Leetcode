class Solution:
    def numSquares(self, n: int) -> int:
        # 能通过，不过挺耗时的。
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, int(i ** 0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        # print(dp)
        return dp[n]

if __name__ == '__main__':
    solu = Solution()
    n = 13
    ans = solu.numSquares(n)
    print(ans)

