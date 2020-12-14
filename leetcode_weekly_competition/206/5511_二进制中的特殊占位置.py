from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        ans = 0
        col1 = []
        for i in range(cols):
            tmp = 0
            for j in range(rows):
                tmp += mat[j][i]
            if tmp == 1:
                col1.append(i)
        # 把列和为1的存储起来。

        for i in range(rows):
            for j in range(cols):
                if sum(mat[i]) != 1:
                    break
                if mat[i][j] == 1 and j in col1:
                    ans += 1
        return ans


solu = Solution()
mat =  [[0,0,0,0,0],
            [1,0,0,0,0],
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]]
ans = solu.numSpecial(mat)
print(ans)