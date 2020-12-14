"""
1219. 黄金矿工
你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。
每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。
为了使收益最大化，矿工需要按以下规则来开采黄金：
每当矿工进入一个单元，就会收集该单元格中的所有黄金。
矿工每次可以从当前位置向上下左右四个方向走。
每个单元格只能被开采（进入）一次。
不得开采（进入）黄金数目为 0 的单元格。
矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。

示例 1：
输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
输出：24
解释：
[[0,6,0],
 [5,8,7],
 [0,9,0]]
一种收集最多黄金的路线是：9 -> 8 -> 7。

示例 2：
输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
输出：28
解释：
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。
提示：
1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
最多 25 个单元格中有黄金。
"""
# 这道题可以用DFS或者回溯来写。
# DFS在解题过程中debug了好久，这里和之前做的DFS不太一样，特别是记录是否访问的数组visited，我们在计算某一个点的最大收益时，
# 计算完成之后务必要还原，也就是刚才访问过的节点还要置为未访问，以便让后面的节点深度遍历到该节点时还可以进行下去。
from typing import List
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:return 0
        m = len(grid)
        n = len(grid[0])
        direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(x, y):
            # 从点(x,y)开始访问，返回其能够获得的最大的收益
            visited[x][y] = True
            tmp = 0
            for i in range(4):
                new_x = x + direction[i][0]
                new_y = y + direction[i][1]
                if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and grid[new_x][new_y] != 0:
                    tmp = max(tmp, dfs(new_x, new_y))
                    visited[new_x][new_y] = False  # 这句搞了半天才发现需要，如果用回溯的框架想会简单很多，
                    # 因为上面是递归一步，这一步就是撤销选择
            return tmp+grid[x][y]

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    visited = [[False] * n for _ in range(m)]
                    ans = max(ans, dfs(i, j))
        return ans

    def getMaximumGold_2(self, grid: List[List[int]]) -> int:
        # 这里练习使用回溯法解决问题
        # 这里的回溯写法其实就是上面的DFS，有时候没搞懂DFS和回溯两者之间的联系和区别。
        return


solu = Solution()
grid = [[0,6,0],[5,8,7],[0,9,0]]
ans = solu.getMaximumGold(grid)
print(ans)






