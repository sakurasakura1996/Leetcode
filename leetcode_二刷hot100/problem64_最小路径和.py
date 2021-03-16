from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 可以不用定义dp，直接在grid改动就行
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[m-1][n-1]


if __name__ == '__main__':
    solu = Solution()
    grid = [[1,2,3],[4,5,6]]
    ans = solu.minPathSum(grid)
    print(ans)