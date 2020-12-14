"""
695. 岛屿的最大面积
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。
注意: 给定的矩阵grid 的长度和宽度都不超过 50。
"""
# 运用dfs来求解，本来看到这个题目以为是问你一共有多少个岛屿，相当于问你总共需要调用多少次外部dfs函数
# 那么这道题就是计算每次外部dfs函数中访问到的1的个数，然后找到其中最大的
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [[-1,0],[0,1],[1,0],[0,-1]]
        if not grid:
            return 0
        ans = 0
        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]

        def dfs(x,y)->int:
            visited[x][y] = 1
            num = 1
            for i in range(4):
                new_x = x + direction[i][0]
                new_y = y + direction[i][1]
                if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and grid[new_x][new_y] == 1:
                    num += dfs(new_x, new_y)
            return num

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    ans = max(ans, dfs(i,j))
        return ans



