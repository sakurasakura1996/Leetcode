"""
221. 最大正方形
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4

示例 2：
输入：matrix = [["0","1"],["1","0"]]
输出：1

示例 3：
输入：matrix = [["0"]]
输出：0
提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] 为 '0' 或 '1'
"""
# 看到这个题目我想了会，最后想到的还是动态规划吧，dp[i][j]表示的是以（i,j）这个点为右下角节点，然后往左上去看，只需要看dp[i-1][j-1]的结果
# 然后再看（i，j）所在的行和列是否也满足情况，如果满足就说明dp[i][j] = dp[i-1][j-1]+1了呀。确实可以解决哎，可以，但是代码写的冗余的很。

# 看了题解之后，突然发现，我的想法还可以改进下，dp[i][j]的大小是可以用dp[i-1][j-1],dp[i][j-1],dp[i-1][j]来确定的啊，三者中的最小值+1即可
# 并不需要像我这样写的太麻烦了。
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        nums = [[max(m, n)] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            num = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    num += 1
                    nums[i][j] = min(nums[i][j], num)
                elif matrix[i][j] == '0':
                    num = 0
                    nums[i][j] = 0
        for j in range(n):
            num = 0
            for i in range(m):
                if matrix[i][j] == '1':
                   num += 1
                   nums[i][j] = min(nums[i][j], num)
                elif matrix[i][j] == '0':
                    num = 0
                    nums[i][j] = 0
        # 边界初始化
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
            ans = max(ans, dp[i][0])
        for j in range(n):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0
            ans = max(ans, dp[0][j])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1' and dp[i-1][j-1] == 0:
                    dp[i][j] = 1
                    ans = max(ans, dp[i][j])
                elif matrix[i][j] == '1' and dp[i-1][j-1] > 0:
                    dp[i][j] = min(dp[i-1][j-1]+1, nums[i][j])
                    ans = max(ans, dp[i][j])
        return ans * ans

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    ans = max(ans, dp[i][j])
        return ans * ans


if __name__ == '__main__':
    solu = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    ans = solu.maximalSquare2(matrix)
    print(ans)