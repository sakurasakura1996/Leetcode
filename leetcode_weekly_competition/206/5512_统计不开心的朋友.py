from typing import List
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        m = len(pairs)


        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n-1):
                idx = preferences[i][j]
                dp[i][idx] = n -1 - j

        ans = set()
        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                pair1 = pairs[i]
                pair2 = pairs[j]
                x, y = pair1[0], pair1[1]
                u, v = pair2[0], pair2[1]
                if (dp[x][u] > dp[x][y] and dp[u][x] > dp[u][v]) or (dp[x][v] > dp[x][y] and dp[v][x] > dp[v][u]):
                    ans.add(x)
                if (dp[y][u] > dp[y][x] and dp[u][y] > dp[u][v]) or (dp[y][v] > dp[y][x] and dp[v][y] > dp[v][u]):
                    ans.add(y)
        return len(ans)


solu = Solution()
n = 6
preferences = [[1,4,3,2,5],[0,5,4,3,2],[3,0,1,5,4],[2,1,4,0,5],[2,1,0,3,5],[3,4,2,0,1]]
pairs = [[3,1],[2,0],[5,4]]

ans = solu.unhappyFriends(n, preferences, pairs)
print(ans)




