"""
5454. 统计全 1 子矩形  显示英文描述
通过的用户数 243
尝试过的用户数 371
用户总通过次数 244
用户总提交次数 434
题目难度 Medium
给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。
示例 1：
输入：mat = [[1,0,1],
            [1,1,0],
            [1,1,0]]
输出：13
解释：
有 6 个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
"""
# 想用动态规划来求解，但是递推关系不能完全推出来
from typing import List
class Solution:
    def numRow(self, row: List[int]) -> int:
        # 计算一横行或者一竖行带有最后一个元素的子矩形全1的个数
        ans = 0
        for i in range(len(row)-1,-1,-1):
            if row[i] == 1:
                ans += 1
            else:
                return ans
        return ans
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        rows = len(mat)
        cols = len(mat[0])
        dp = [[0] * (cols+1) for _ in range(rows+1)]
        # 边界处理
        for i in range(1,cols+1):
            dp[0][i] = self.numRow(mat[0][:])

        for j in range(1, rows+1):
            dp[i][0] = self.numRow(mat[:][0])

        if


