
import sys

class Solution:
    def shortestPath(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        ans = []
        path = []
        dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(x, y):
            visited[x][y] = True
            path.append((x, y))
            if x == m - 1 and y == n - 1:
                ans.append(path.copy())
            for i in range(4):
                new_x = x + dir[i][0]
                new_y = y + dir[i][1]
                if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and not matrix[new_x][new_y]:
                    dfs(new_x, new_y)
            visited[x][y] = False
            path.pop()

        dfs(0, 0)
        return ans


if __name__ == '__main__':
    while True:
        try:
            m, n = sys.stdin.readline().strip().split()
            m = int(m)
            n = int(n)
            matrix = []
            for i in range(m):
                temp = sys.stdin.readline().strip().split()
                temp = [int(x) for x in temp]
                matrix.append(temp.copy())

            solu = Solution()
            ans = solu.shortestPath(matrix)
            idx = 0
            length = float('inf')
            for i, path in enumerate(ans):
                if len(path) < length:
                    idx = i
            for item in ans[i]:
                print(item)

        except:
            break









