"""
旋转矩阵：给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
不占用额外内存空间能否做到？
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-matrix-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead
		好像发现不占用额外内存的规律了。先把内部List的顺序倒置一下，然后以对角线互换
		"""
		m = len(matrix)
		# matrix = [matrix[i] for i in reversed(range(m))]  这样写有问题，有点像视图那种感觉，就是查看的时候是换位置了，但是后面又复原了
		for i in range(int(m/2)):
			for j in range(m):
				tmp = matrix[i][j]
				matrix[i][j] = matrix[m-i-1][j]
				matrix[m-i-1][j] = tmp

		for i in range(m):
			for j in range(i,m):
				tmp = matrix[i][j]
				matrix[i][j] = matrix[j][i]
				matrix[j][i] = tmp






matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

solu = Solution()
solu.rotate(matrix)
print(matrix)