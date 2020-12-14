"""
面试题 16.19. 水域大小
你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。
池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。
示例：
输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]
提示：
0 < len(land) <= 1000
0 < len(land[i]) <= 1000
"""
# 这个题就像我在problem695中说的一样，问题方式可以用这题的，多少个相邻部分，各位多大
from typing import List
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        direction = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        if not land:
            return []
        n = len(land)
        m = len(land[0])
        visited = [[0] * m for _ in range(n)]
        ans = []

        def dfs(x,y)->int:
            visited[x][y] = 1
            num = 1
            for i in range(8):
                new_x = x + direction[i][0]
                new_y = y + direction[i][1]
                if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and land[new_x][new_y] == 0:
                    num += dfs(new_x,new_y)
            return num

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and land[i][j] == 0:
                    num = dfs(i,j)
                    ans.append(num)
        ans.sort()
        return ans


solu = Solution()
land = [
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
ans = solu.pondSizes(land)
print(ans)