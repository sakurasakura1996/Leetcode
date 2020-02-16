"""
杨辉三角二
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

进阶：
你可以优化你的算法到 O(k) 空间复杂度吗？
"""
# 首先比较自然的想法那当然是直接把上一题杨辉三角的题目拿过来，然后取出第k行就行了
# 然后，可以在想空间复杂度为 O(k)的算法

# way 1
# from typing import List
# import numpy as np
# class Solution:
#     def getRow(self,rowIndex: int) -> List[int]:
#         answer = []
#         for i in range(rowIndex+1):
#             lis = list(np.ones(i + 1).astype(int))  # 注意这里的变量名千万不要起名为 list
#             answer.append(lis)
#         for i in range(rowIndex+1):
#             for j in range(i+1):
#                 if j == 0 or j == i:
#                     answer[i][j] = 1
#                 else:
#                     answer[i][j] = answer[i-1][j-1] + answer[i-1][j]
#         return answer[rowIndex]



# way 2
# 当然这个题目的意义就在于用O(k)的空间复杂度来做
# 观察发现，这k个值，是对称的，所以只需要求出前一半，然后后面的只需要对称着写就行。然后第k行的值是由第k-1行的值求得而来
# 如果是从前往后计算的话，会导致前一行的值被替代，所以从第k行中间的值开始计算，从后往前，就不会产生数值冲突了

from typing import List
import numpy as np
class Solution:
    def getRow(self,rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        answer = list(np.ones(rowIndex+1).astype(int))
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                answer[j] = answer[j] + answer[j-1]
            # # 已经写下了一半的值，后面一半的直接copy下来
            # for j in range(rowIndex,int((rowIndex+1)/2),-1):
            #     answer[j] = answer[rowIndex-j]
        return answer

solu = Solution()
answer = solu.getRow(4)
print(answer)