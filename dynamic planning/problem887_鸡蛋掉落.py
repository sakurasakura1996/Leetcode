"""
887. 鸡蛋掉落
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
你的目标是确切地知道 F 的值是多少。
无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
示例 1：
输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。

示例 2：
输入：K = 2, N = 6
输出：3
示例 3：
输入：K = 3, N = 14
输出：4
提示：
1 <= K <= 100
1 <= N <= 10000
"""
from functools import lru_cache
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        @lru_cache(None)
        def dp(k, n):
            if k == 1:
                return n
            if n == 0 or n == 1:
                return n
            import sys
            ans = sys.maxsize
            for i in range(1, n+1):
                ans = min(ans, max(dp(k-1, i-1), dp(k, n-i))+1)
            return ans

        res = dp(K, N)
        return res

    def superEggDrop2(self, K: int, N: int)->int:
        memo = dict()
        def dp(k, n):
            if k == 1:return n
            if n == 0:return 0
            if (k, n) in memo:
                return memo[(k, n)]
            res = float("INF")
            for i in range(1, N+1):
                res = min(res, max(dp(k, n-i), dp(k-1, i-1))+1)
            memo[(k,n)] = res
            return res
        return dp(K, N)
    # 上面两种方法都超出时间了，应该是递归过深了。
    # 下面这个方法还是超时了。
    def superEggDrop3(self, K: int, N: int) -> int:

        dp = [[0] * (N+1) for _ in range(K+1)]
        # 边界初始化
        # for i in range(N+1):
        #     dp[1][i] = i
        # for i in range(K):
        #     dp[i][0] = 0
        #     dp[i][1] = 1
        for i in range(K+1):
            for j in range(N+1):
                if i == 1:
                    dp[i][j] = j
                if j == 1 or j == 0:
                    dp[i][j] = j
                dp[i][j] = j
                for k in range(1, j+1):
                    dp[i][j] = min(dp[i][j], max(dp[i-1][k-1]+1, dp[i][j-k]+1))
        return dp[K][N]

    def superEggDrop4(self, K: int, N: int) -> int:
        def f(m, k):
            if k == 0 or m == 0:return 0
            return f(m-1, k-1) + 1 + f(m-1, k)
        m = 0
        while f(m, K) < N:
            m += 1
        return m

    def superEggDrop4(self, K: int, N: int) -> int:
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        m = 0
        while dp[m][K] < N:
            m += 1
            for i in range(1, K + 1):
                dp[m][i] = dp[m - 1][i - 1] + 1 + dp[m - 1][i]
        return m




solu = Solution()
ans = solu.superEggDrop4(4, 5000)
print(ans)
