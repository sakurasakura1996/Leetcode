"""
74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
输出：true
示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
输出：false
示例 3：
输入：matrix = [], target = 0
输出：false
提示：
m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
# 因为行与行之间存在严格的大小关系，所以我的第一想法就是把二维转换成一维的然后直接用二分搜索就可以了。这样的空间复杂度较高。
# 直接定义一个新数组可以通过，这里还是说一下不定义数组的方法，主要还是想清楚不定义数组时的转换关系，mid求出来之后，取matrix
# 中的值的时候，将mid转换为matrix的行和列的值，row = mid // n, col = mid % n就行了。
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        dp = []
        for i in range(m):
            dp.extend(matrix[i])

        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right) // 2
            if dp[mid] == target:
                return True
            elif dp[mid] < target:
                left = mid+1
            else:
                right = mid - 1
        return False


if __name__ == '__main__':
    solu = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 3
    ans = solu.searchMatrix(matrix, target)
    print(ans)
