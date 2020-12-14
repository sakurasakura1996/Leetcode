"""
面试题 08.12. 八皇后
设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。
这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。
注意：本题相对原题做了扩展
示例:
 输入：4
 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def could_place(row, col):
            return not (cols[col] + hill_diagonsals[row - col] + dale_diagonsals[row + col])

        def place_queen(row, col):
            cols[col] = 1
            hill_diagonsals[row - col] = 1
            dale_diagonsals[row + col] = 1
            queens.add((row, col))

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            ans.append(solution)

        def remove_queen(row, col):
            cols[col] = 0
            hill_diagonsals[row - col] = 0
            dale_diagonsals[row + col] = 0
            queens.remove((row, col))

        def backtrack(row=0):
            for col in range(n):
                if could_place(row,col):
                    place_queen(row,col)
                    if row+1 == n:
                        add_solution()
                    else:
                        backtrack(row+1)
                    remove_queen(row, col)

        cols = [0] * n
        hill_diagonsals = [0] * (2 * n - 1)
        dale_diagonsals = [0] * (2 * n - 1)
        queens = set()
        ans = []
        backtrack()
        return ans