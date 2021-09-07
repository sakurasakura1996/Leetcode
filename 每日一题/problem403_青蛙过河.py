from functools import lru_cache
from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # 看到该题目，感觉看上去应该是 动态规划题, 难点在于，当前点能到达可能是从
        # 不同的节点跳跃过来，然后跳跃的步幅也不一样。
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True

        # 先判断如果两个相邻石头直接的距离过大，就直接可以返回False了
        for i in range(1, n):
            if stones[i] - stones[i-1] > i:
                return False

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                # 这里j要倒序遍历，主要是因为递推公式的原因。
                k = stones[i] - stones[j]
                if k > j + 1:
                    break
                dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]
                if i == n - 1 and dp[i][k]:
                    return True

            # 我们要想清楚，为什么下面的j顺序遍历是不行的，不是简单的因为递推公式。
            # for j in range(i):
            #     k = stones[i] - stones[j]
            #     if k > j + 1:
            #         break
            #     dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]
            #     if i == n - 1 and dp[i][k]:
            #         return True
        return False

    def canCross2(self, stones: List[int]) -> bool:
        # 回溯法和暴力搜索有点类似，我们在当前节点，有一个step，可以选择step-1,step,step+1
        # 三种选择，遍历循环，然后不但递归搜索，如果能到达最后一个石头直接返回true就行了。
        # 超时问题，可以用记忆化，备忘录的方法来解决。
        n = len(stones)
        if stones[1] != 1:
            return False

        @lru_cache(None)
        def backtrace(cur, path):
            if cur == stones[-1]:
                return True
            for i in range(max(1, path-1), path+2):
                if cur+i in stones:
                    if backtrace(cur+i, i):
                        return True
            return False

        ans = backtrace(1, 1)
        return ans


if __name__ == '__main__':
    solu = Solution()
    stones = [0,1,2,3,4,8,9,11]
    ans = solu.canCross2(stones)
    print(ans)






