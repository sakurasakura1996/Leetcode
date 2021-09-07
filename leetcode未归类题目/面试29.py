"""
面试题29.顺时针打印矩阵。
和主站54题相同
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
"""
# 总体而言，还是第一种方法大家都能直接想到，但是第一种方法我自己写的太不顺畅了，思考和编码过程都太长时间了。
# way1
# from typing import List
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if len(matrix)==0 or len(matrix[0]) == 0:
#             return []
#         visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
#
#         ans = []
#         dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         num = 0
#         cur_dir = 0
#         x,y = 0,0
#         while num < len(matrix) * len(matrix[0]):
#             ans.append(matrix[x][y])
#             visited[x][y] = 1
#             new_x = x + dir[cur_dir][0]
#             new_y = y + dir[cur_dir][1]
#             if new_x < len(matrix) and new_y < len(matrix[0]) and not visited[new_x][new_y]:
#                 x = new_x
#                 y = new_y
#             else:
#                 # 换个方向
#                 cur_dir += 1
#                 cur_dir = cur_dir%4
#                 x = x + dir[cur_dir][0]
#                 y = y + dir[cur_dir][1]
#             num += 1
#         return ans


# way2
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows, columns = len(matrix), len(matrix[0])
        ans = []
        left, right, top, bottom = 0, columns-1, 0, rows-1
        while left <= right and top <= bottom:
            for column in range(left, right+1):
                ans.append(matrix[top][column])
            for row in range(top+1, bottom+1):
                ans.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    ans.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    ans.append(matrix[row][left])
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return ans


solu = Solution()
matrix = [[3, 3, 4, 5]]
ans = solu.spiralOrder(matrix)
print(ans)


