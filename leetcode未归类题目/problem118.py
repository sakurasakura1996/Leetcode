"""
杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前numRows行

"""
from typing import List
import numpy as np
class Solution:
    def generate(self,numRows: int) -> List[List[int]]:
        answer = []
        for i in range(numRows):
            lis = list(np.ones(i+1).astype(int))   # 注意这里的变量名千万不要起名为 list
            answer.append(lis)
        for i in range(numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    answer[i][j] = 1
                else:
                    answer[i][j] = answer[i-1][j-1] + answer[i-1][j]
        return answer

solu = Solution()
ans = solu.generate(5)
print(ans)