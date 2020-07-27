"""
1252. 奇数值单元格的数目
给你一个 n 行 m 列的矩阵，最开始的时候，每个单元格中的值都是 0。
另有一个索引数组 indices，indices[i] = [ri, ci] 中的 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。
你需要将每对 [ri, ci] 指定的行和列上的所有单元格的值加 1。
请你在执行完所有 indices 指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。
输入：n = 2, m = 3, indices = [[0,1],[1,1]]
输出：6
解释：最开始的矩阵是 [[0,0,0],[0,0,0]]。
第一次增量操作后得到 [[1,2,1],[0,1,0]]。
最后的矩阵是 [[1,3,1],[1,3,1]]，里面有 6 个奇数。
"""
# 在纸上总结出了公式，那就是奇数行的个数*n + 奇数列的个数*m - 2*奇数列个数*奇数行个数
from typing import List
from collections import Counter
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row_num_counter = Counter()
        col_num_counter = Counter()
        if not indices:
            return 0
        indices_len = len(indices)
        for i in range(indices_len):
            r, c = indices[i]
            if r not in row_num_counter:
                row_num_counter[r] = 1
            else:
                row_num_counter[r] += 1
            if c not in col_num_counter:
                col_num_counter[c] = 1
            else:
                col_num_counter[c] += 1

        odd_row = 0
        odd_col = 0
        for key,value in row_num_counter.items():
            if value%2 == 1:
                odd_row += 1
        for key,value in col_num_counter.items():
            if value%2 == 1:
                odd_col += 1
        return odd_row*m + odd_col*n - 2*odd_row*odd_col


solu = Solution()
indices = [[40,5]]
ans = solu.oddCells(48,37,indices)
print(ans)

