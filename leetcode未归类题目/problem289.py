"""
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。


示例：
输入： 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出：
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
"""
import numpy as np
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]):
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        board_plus = np.zeros((m+2, n+2),dtype=int)
        board_plus[1:m+1,1:n+1] = board
        for i in range(m):
        	for j in range(n):
        		board[i][j] = int(board_plus[i][j]+board_plus[i][j+1]+board_plus[i][j+2]+board_plus[i+1][j]
        		+board_plus[i+1][j+2]+board_plus[i+2][j]+board_plus[i+2][j+1]+board_plus[i+2][j+2])
        		# print(board_plus[i+1][j+1], board[i][j])
        		if board_plus[i+1][j+1] == 1:
        			if board[i][j] <2:
        				board[i][j] =0
        			if board[i][j] == 2:
        				board[i][j] = 1
        			if board[i][j] == 3:
        				board[i][j] = 1
        			if board[i][j] > 3:
        				board[i][j] = 0
        		elif board_plus[i+1][j+1] == 0:
        			if board[i][j] == 3:
        				board[i][j] = 1
        			else:
        				board[i][j] = 0


        		# if int(board_plus[i+1][j+1]) == 1 and board[i][j] < 2:
        		# 	board[i][j] = 0
        		# if int(board_plus[i+1][j+1]) == 1 and board[i][j] == 2:
        		# 	board[i][j] = 1
        		# if int(board_plus[i+1][j+1]) == 1 and board[i][j] == 3:
        		# 	board[i][j] = 1
        		# if int(board_plus[i+1][j+1]) == 1 and board[i][j] > 3:
        		# 	board[i][j] = 0
        		# if int(board_plus[i+1][j+1]) == 0 and board[i][j] ==3:
        		# 	board[i][j] = 1
        		# else:
        		# 	board[i][j] = 0
        		# 	这里的表达是错误的，这么简答的做半天。
        # return board_plus

board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

solu = Solution()
board_plus = solu.gameOfLife(board)
