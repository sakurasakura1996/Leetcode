from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(x, y):
            visited[x][y] = True
            for i in range(4):
                new_x = x + dir[i][0]
                new_y = y + dir[i][1]
                if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and grid[new_x][new_y] == '1':
                    dfs(new_x, new_y)
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        return ans

    def numIslands2(self, grid: List[List[str]]) -> int:
        # 经常用DFS来写，还是得熟悉下BFS怎么写啊。
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    grid[i][j] = '0'
                    neighbors = deque([(i, j)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                                neighbors.append((x,y))
                                grid[x][y] = '0'
        return ans


if __name__ == '__main__':
    solu = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    ans = solu.numIslands(grid)
    print(ans)

