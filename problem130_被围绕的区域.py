"""
130. 被围绕的区域
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""
# 我的思路是把边界上存在的0找出来然后进行DFS，他们访问到的都进行标记已访问，然后再遍历一遍数组，未访问到的‘O'都标记为X
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board:
            return

        n = len(board)
        m = len(board[0])
        visited = [[0] * m for _ in range(n)]

        direction = [[-1,0],[0,1],[1,0],[0,-1]]


        def dfs(x,y):
            visited[x][y] = 1
            for i in range(4):
                new_x = x + direction[i][0]
                new_y = y + direction[i][1]
                if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and board[new_x][new_y] == 'O':
                    dfs(new_x, new_y)

        for i in range(n):
            if board[i][0] == 'O' and not visited[i][0]:
                dfs(i,0)
            if board[i][m-1] == 'O' and not visited[i][m-1]:
                dfs(i, m-1)

        for i in range(m):
            if board[0][i] == 'O' and not visited[0][i]:
                dfs(0, i)
            if board[n-1][i] == 'O' and not visited[n-1][i]:
                dfs(n-1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'


solu = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solu.solve(board)
print(board)