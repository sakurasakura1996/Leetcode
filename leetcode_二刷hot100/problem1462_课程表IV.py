from typing import List
class Solution:
    # 大佬们说，这道题不用BFS或者DFS，本质上是弗洛伊德多源最短路径的简化版。
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[False] * n for _ in range(n)]
        # every edge
        for u, v in prerequisites:
            dp[u][v] = True

        # dp里面装着dp[i][j][k-1]的结果
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])

        return [dp[u][v] for u, v in queries]


if __name__ == '__main__':
    solu = Solution()
    n = 2
    prerequisites = [[1, 0]]
    queries = [[0, 1], [1, 0]]
    ans = solu.checkIfPrerequisite(n, prerequisites, queries)
    print(ans)