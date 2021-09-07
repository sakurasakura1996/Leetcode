from typing import List
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # 如果用图来表示的话，a信任b，就应该a->b,那么如果存在法官，该法官的入度为N-1，出度为0.
        in_degrees = [0] * N
        out_degrees = [0] * N
        for a, b in trust:
            out_degrees[a - 1] += 1
            in_degrees[b - 1] += 1
        ans = -1
        num = 0
        for i in range(N):
            if in_degrees[i] == N - 1 and out_degrees[i] == 0:
                num += 1
                ans = i + 1
        if num > 1:
            return -1
        return ans
