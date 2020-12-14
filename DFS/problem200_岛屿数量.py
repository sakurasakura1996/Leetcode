"""
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例 1:
输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1
示例 2:
输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
"""
# 这道题还是不难的，我们直接dfs陆地，访问过的用visited数组来记录下来。
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]
        direction = [[-1,0],[0,1],[1,0],[0,-1]]
        def dfs(x,y):
            visited[x][y] = 1
            for i in range(4):
                new_x = x + direction[i][0]
                new_y = y + direction[i][1]
                if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and grid[new_x][new_y] == '1':
                    dfs(new_x, new_y)

        ans = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans