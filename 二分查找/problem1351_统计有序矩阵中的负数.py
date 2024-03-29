"""
1351. 统计有序矩阵中的负数
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。

请你统计并返回 grid 中 负数 的数目。



示例 1：

输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。
示例 2：

输入：grid = [[3,2],[1,0]]
输出：0
示例 3：

输入：grid = [[1,-1],[-1,-1]]
输出：3
示例 4：

输入：grid = [[-1]]
输出：1


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100


进阶：你可以设计一个时间复杂度为 O(n + m) 的解决方案吗？
"""
# 这题还是不难的，简单题估计你直接暴力遍历就可以通过，这个 O（n+m)的方案也不是很难想，直接从右上角或者左下角来开始搜索
from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = 0
        col = n - 1
        ans = 0
        while row < m and col >= 0:
            if grid[row][col] < 0:
                ans += (m - row)
                col -= 1
            elif grid[row][col] >= 0:
                row += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    grid = [[-1]]
    ans = solu.countNegatives(grid)
    print(ans)