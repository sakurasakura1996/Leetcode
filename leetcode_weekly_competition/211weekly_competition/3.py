from typing import List
from functools import lru_cache
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        infor = []
        for s, a in zip(scores, ages):
            infor.append([a, s])
        infor = sorted(infor)

        @lru_cache(None)
        def solve(pos=len(scores)-1, ceiling=1e9):
            if pos < 0:
                return 0
            at, st = infor[pos]
            if st > ceiling:
                return solve(pos-1, ceiling)
            to_ret = st + solve(pos - 1, min(ceiling, st))
            to_ret = max(to_ret, solve(pos - 1, ceiling))

            return to_ret
        return solve()

    def bestTeamScore2(self, scores: List[int], ages: List[int]) -> int:
        infor = []
        for s, a in zip(scores, ages):
            infor.append([a, s])
        infor = sorted(infor)
        # print(infor)
        dp = [0] * len(scores)
        for i in range(len(scores)):
            dp[i] = infor[i][1]
            for j in range(i):
                if infor[i][1] >= infor[j][1]:
                    dp[i] = max(dp[i], dp[j]+infor[i][1])
        return max(dp)


solu = Solution()
scores = [1,3,5,10,15]
ages = [1,2,3,4,5]
ans = solu.bestTeamScore2(scores, ages)
print(ans)