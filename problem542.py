#  01矩阵
#  给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
# 两个相邻元素间的距离为 1 。
# 示例 1: 
# 输入:
# 0 0 0
# 0 1 0
# 0 0 0
# 输出:
# 0 0 0
# 0 1 0
# 0 0 0
from typing import List
import numpy as np
# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#     	m = len(matrix)
#     	n = len(matrix[0])
#     	ans = np.ones((m,n),dtype=int) * 10000
    	
#     	def dfs(x,y):
#     		for i in range(m):
#     			for j in range(n):
#     				if matrix[i][j] == 1:
#     					ans[i][j] = min(ans[i][j],abs(i-x)+abs(j-y))
#     	for i in range(m):
#     		for j in range(n):
#     			if matrix[i][j] == 0:
#     				ans[i][j] = 0
#     				dfs(i,j)
#     	return ans
#  
# 以下方法时间超时了。   	
# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#     	m = len(matrix)
#     	n = len(matrix[0])
#     	ans = np.ones((m,n),dtype=int) * 10000
    	
#     	def dfs(x,y):
#     		for i in range(m):
#     			for j in range(n):
#     				if matrix[i][j] == 1:
#     					ans[i][j] = min(ans[i][j],abs(i-x)+abs(j-y))
#     	for i in range(m):
#     		for j in range(n):
#     			if matrix[i][j] == 0:
#     				ans[i][j] = 0
#     			else:  # 如果值为1的话，那么就看看四周有无0，有的话就是1，没的话就是
#     				dfs(i,j)
#     	return ans


# 下面的代码把我搞晕了，最后还是错的，不得不说自己的思考方式实在太蠢了，显然这个代码的逻辑不对，改了这里那里错了，改了那里这里又错了
# class Solution:
# 	def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
# 		m = len(matrix)
# 		n = len(matrix[0])
# 		for i in range(m):
# 			for j in range(n):
# 				if matrix[i][j] != 0:
# 					if i>0 and j>0:
# 						matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1])+1
# 					if i>0 and j==0:
# 						matrix[i][j] = matrix[i-1][j]+1
						
# 					if j>0 and i==0:
# 						matrix[i][j] = matrix[i][j-1]+1
						
# 		print(matrix)	
# 		for i in range(m-1,-1,-1):
# 			for j in range(n-1,-1,-1):
			
# 				if matrix[i][j] != 0:
# 					if i<m-1 and j<n-1:
# 						if matrix[i][j]>min(matrix[i+1][j],matrix[i][j+1]):
# 							matrix[i][j] = min(matrix[i+1][j],matrix[i][j+1])+1
# 					if i<m-1 and j==n-1:
# 						if matrix[i][j]>matrix[i+1][j]:
# 							matrix[i][j] = matrix[i+1][j]+1
# 					if j<n-1 and i==m-1:
# 						if matrix[i][j]>matrix[i][j+1]:
# 							matrix[i][j] = matrix[i][j+1]+1
# 		return matrix

# class Solution:
# 	def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
# 		m = len(matrix)
# 		n = len(matrix[0])
# 		for i in range(m):
# 			for j in range(n):
# 				if matrix[i][j] != 0:
# 					if i>0 and j>0:
# 						matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1])+1
# 					if i>0 and j==0:
# 						matrix[i][j] = matrix[i-1][j]+1			
# 					if j>0 and i==0:
# 						matrix[i][j] = matrix[i][j-1]+1

# 		for i in range(m-1,-1,-1):
# 			for j in range(n-1,-1,-1):
# 				r,b = 10001,10001
# 				if matrix[i][j] != 0:
# 					if i < m - 1:
# 						b = matrix[i + 1][j]
# 					if j < n - 1:
# 						r = matrix[i][j + 1]
# 					matrix[i][j] = min(matrix[i][j], min(r,b) + 1)
# 		return matrix
# 经典的BFS解法，一定要熟悉熟悉BFS和队列栈这些数据结构的使用
class Solution:
	def updateMatrix(self, matrix: List[List[int]])->List[List[int]]:
		res = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))] # 设定结果集
		q = collections.deque()   # BFS 经典结果，设定一个queue来存储每个层次上的点
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j]==0:  # 将题目转换为 0 到其他点的距离
					res[i][j]=0
					q.append([i,j])
		whild q:
			x, y = q.popleft()
			for x_bias, y_bias in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
				new_x = x + x_bias
				new_y = y + y_bias
				if 0<=new_x<len(matrix) and 0<=new_y<len(matrix[0]) and res[new_x][new_y]==None:
					res[new_x][new_y] = res[x][y]+1
					q.append([new_x][new_y])
		return res


solu = Solution()
matrix = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
# matrix = [[0, 0, 0],[0, 1, 0],[1,1,1]]
ans = solu.updateMatrix(matrix)
print(ans)

