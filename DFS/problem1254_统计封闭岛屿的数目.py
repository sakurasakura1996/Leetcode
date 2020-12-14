"""
1254. 统计封闭岛屿的数目
有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。
我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。
如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。
请返回封闭岛屿的数目。
示例 1：
输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
示例 2：
输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
输出：1
示例 3：
输入：grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
输出：2
提示：
1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""
# 注意题目中表达的封闭岛屿的概念，必须四周相邻的都被水域包围才算是封闭岛屿，比如边界上的陆地并不是岛屿了
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 这道题化的时间还挺久的，可以熟悉一下，最后想的方法是，我们把grid中值为1的都标记为以访问，然后再访问长方形
        # 的边界，如果是0，那就对他进行dfs，访问到的0都置为以访问，然后接下来开始计算答案了。
        # 我们循环遍历一遍，如果为0而且还没有被访问到的，对其进行dfs，算一次结果，最后返回调用了几次这样的dfs就是答案
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]
        direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(x, y):
            visited[x][y] = 1
            for i in range(4):
                new_x = x + direction[i][0]
                new_y = y + direction[i][1]
                if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and grid[new_x][new_y] == 0:
                    visited[new_x][new_y] = 1
                    dfs(new_x, new_y)

        ans = 0
        for i in range(m):
            if grid[0][i] == 0 and not visited[0][i]:
                dfs(0, i)
            if grid[n - 1][i] == 0 and not visited[n - 1][i]:
                dfs(n - 1, i)
        for i in range(n):
            if grid[i][0] == 0 and not visited[i][0]:
                dfs(i, 0)
            if grid[i][m - 1] == 0 and not visited[i][m - 1]:
                dfs(i, m - 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and not visited[i][j]:
                    dfs(i, j)
                    ans += 1
        return ans


solu = Solution()
grid = [[1,1,1,1,1,1,1],
[1,0,0,0,0,0,1],
[1,0,1,1,1,0,1],
[1,0,1,0,1,0,1],
[1,0,1,1,1,0,1],
[1,0,0,0,0,0,1],
[1,1,1,1,1,1,1]]

ans = solu.closedIsland(grid)
print(ans)
