from functools import lru_cache
class Solution:
    @lru_cache(None)
    def numWays(self, steps: int, arrLen: int) -> int:
        # 回溯肯定尼玛超时啊。arrLen 可以到10^6, 但是 steps最大只能到500
        # 不行啊，还是会超时，但是加上备忘录就可以了，
        @lru_cache(None)
        def backtrace(step, idx):
            # 当前在idx节点 还剩step可以走的时候,请问有多少种走法最后在原点
            if idx < 0 or idx >= arrLen:
                return 0
            if step == idx:
                return 1
            elif step < idx:
                return 0
            else:
                return backtrace(step-1, idx-1) + backtrace(step-1, idx) + backtrace(step-1, idx+1)

        ans = backtrace(steps, 0)
        return ans

    def numWays(self, steps: int, arrLen: int) -> int:
        # 有预感应该需要动态规划思想来
        mod = 10 ** 9 + 7
        maxColumn = min(arrLen - 1, steps)

        dp = [[0] * (maxColumn + 1) for _ in range(steps + 1)]
        dp[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(0, maxColumn + 1):
                dp[i][j] = dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
                if j + 1 <= maxColumn:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod

        return dp[steps][0]


if __name__ == '__main__':
    solu = Solution()
    steps = 4
    arrLen = 2
    ans = solu.numWays(steps, arrLen)
    print(ans)





