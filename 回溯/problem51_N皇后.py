"""
51. N皇后
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
上图为 8 皇后问题的一种解法。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
示例:
输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
提示：
皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。
当然，她横、竖、斜都可走一到七步，可进可退。
"""
# 这道题是比较经典的题目,用于练习回溯法的编码。我们要仔细思考回溯法的解题模板，然后对应着去写
# 每行有一个皇后，每列也只能有一个皇后。斜方向上也只能有一个皇后。
# 这道题的回溯过程比较复杂，所以编码如果思路不好的话还是容易写不出来。
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            ans.append(solution)

        def remove_queen(row, col):
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0
            queens.remove((row, col))


        def backtrack(row=0):
            for col in range(n):   # col
                if could_place(row, col):
                    place_queen(row, col)
                    if row+1 == n:
                        add_solution()
                    else:
                        backtrack(row+1)
                    remove_queen(row, col)

        # 题目较为让人混乱的点就是这几个列表，我们为了检查当前点(row, col)是否可以作为皇后点的话，需要看看这一点同一行内，两个斜方向上
        # 是否有皇后了，斜方向上总共有（2n-）个斜行，然后如何确定 点(row, col)所在的两个方向的斜行也是比较重要的，尤其时下文的
        # hill_diagonals 位置确定的方法是自己定义的。利用row-col
        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        ans = []
        backtrack()
        return ans


solu = Solution()
ans = solu.solveNQueens(4)
print(ans)






