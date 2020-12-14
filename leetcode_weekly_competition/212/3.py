from typing import List
from functools import lru_cache
import sys
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # 感觉动态规划不行，回溯我又不太熟
        rows = len(heights)
        cols = len(heights[0])

        visited = [[False] * cols for _ in range(rows)]
        dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        @lru_cache(None)
        def dfs(x, y):
            if x == rows - 1 and y == cols - 1:
                return 0
            ans = sys.maxsize
            visited[x][y] = True
            for i in range(4):
                new_x = x + dir[i][0]
                new_y = y + dir[i][1]
                if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y]:
                    delta = abs(heights[new_x][new_y] - heights[x][y])
                    ans = min(ans, max(delta, dfs(new_x, new_y)))
                    # visited[new_x][new_y] = False
            visited[x][y] = False

            return ans
        return dfs(0, 0)

    def minimumEffortPath2(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        left = 0
        right = 0
        dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        # 下面注释的方法求出的区间边界有问题
        # for i in range(rows):
        #     max_right = max(max_right, max(heights[i]))
        #     min_right = min(min_right, min(heights[i]))
        # right = max_right - min_right
        for i in range(rows):
            for j in range(1, cols):
                right = max(right, abs(heights[i][j] - heights[i][j-1]))
        for i in range(cols):
            for j in range(1, rows):
                right = max(right, abs(heights[j][i] - heights[j-1][i]))

        # 然后用二分法来不断check k值
        def check(x, y, k, visited):
            # 判断是否有一条路径满足差值绝对值最大值不大于k。
            if x == rows - 1 and y == cols - 1:
                return True
            visited[x][y] = True
            for i in range(4):
                new_x = x + dir[i][0]
                new_y = y + dir[i][1]
                if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and \
                    abs(heights[x][y] - heights[new_x][new_y]) <= k:
                    if check(new_x, new_y, k, visited):
                        return True
            return False

        while left < right:
            mid = (left + right) // 2
            visited = [[False] * cols for _ in range(rows)]
            if not check(0, 0, mid, visited):
                left = mid + 1
            else:
                right = mid
        return left

    def minimumEffortPath3(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        visited = [[False] * cols for _ in range(rows)]

        




solu = Solution()
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
ans = solu.minimumEffortPath2(heights)
print(ans)





