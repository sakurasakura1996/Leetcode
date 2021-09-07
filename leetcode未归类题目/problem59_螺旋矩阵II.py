from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 我们就仿照一个蚂蚁走路的过程就行了嘛, 我们按照 右 下 左 上的顺序来走路，先定义好方向（用dir来存储) 如果当前可以继续沿着此方向
        # 走的话，那我们就要继续往这个方向走，如果走不下去了，那么换个方向就行。
        ans = [[0] * n for _ in range(n)]
        direction = [[0, 1],[1, 0],[0, -1],[-1, 0]]
        dir = 0
        x = y = 0
        num = 1
        while num <= n * n:
            ans[x][y] = num
            num += 1
            new_x = x + direction[dir][0]
            new_y = y + direction[dir][1]
            if 0 <= new_x < n and 0 <= new_y < n and ans[new_x][new_y] == 0:
                x = new_x
                y = new_y
            else:
                dir = (dir + 1) % 4
                x = x + direction[dir][0]
                y = y + direction[dir][1]
        return ans


if __name__ == '__main__':
    solu = Solution()
    ans = solu.generateMatrix(4)
    print(ans)
