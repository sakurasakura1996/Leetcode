"""
剑指 Offer 04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。

限制：
0 <= n <= 1000
0 <= m <= 1000
注意：本题与主站 240 题相同
"""
# 斜向查找的话，时间复杂度是O(max(N,M))错了错了，又不是正方形结构，所以说不好。
# 后面在纸上画着画着发现了一个O(N+M)复杂度的方法，那就是从左下角开始和target比较，如过小于target就向上走
# 如果大于target就向右走。
from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        x = m-1
        y = 0
        while 0 <= x < m and 0 <= y < n:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                x -= 1
            else:
                y += 1
        return False

    # 二分法，当时脑海中有这个想法，但是没有想出来确切的解决方法。二维二分搜索其实工作原理和普通的二分搜索一样，但是需要同时搜索二维数组的行和列
    def findNumberIn2DArray2(self, matrix: List[List[int]], target: int) -> bool:
        


if __name__ == '__main__':
    solu = Solution()
    matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    ans = solu.findNumberIn2DArray(matrix, 20)
    print(ans)
