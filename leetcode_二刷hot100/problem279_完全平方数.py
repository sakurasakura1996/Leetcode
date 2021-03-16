import math
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, 101):
            if i * i <= n:
                squares.append(i*i)
            else:
                break

        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            end = int(math.sqrt(i))
            for j in range(end):
                dp[i] = min(dp[i], dp[i-squares[j]]+1)
        return dp[n]


if __name__ == '__main__':
    solu = Solution()
    n = 12
    ans = solu.numSquares(n)
    print(ans)