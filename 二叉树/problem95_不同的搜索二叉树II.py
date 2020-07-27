""""
95. 不同的二叉搜索树 II
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
示例：
输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
提示：
0 <= n <= 8
problem96和这题是同一个题目，只不过它只需要输出一个不同结构二叉搜索树的个数，这个题目是要输出所有可能结果,递归是比较好思考的方法
"""
from typing import List
from functools import lru_cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val =val
        self.left = left
        self.right = right

class Solution:
    # 这道题和96题虽然题意相同，但是不能使用动态规划了
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        def helper(start, end):
            if start > end:
                return [None]
            ans = []
            for i in range(start, end+1):
                leftTrees = helper(start,i-1)
                rightTrees = helper(i+1,end)

                for l in leftTrees:
                    for r in rightTrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
        ans = helper(1,n)
        return ans

    def generateTrees(self, n:int):
        # woca,这道题还是可以用动态规划来写哎
        """
        标准的动态规划，最标准的，还没有优化，适合初学者的。
        1.定义dp数组，dp[i][j] 存储数字为i---j之间的所有可能的情况,dp为三维数组
        2.规定初始值，如果i==j,表示只有一个节点的情况，添加节点val为i即可，
        i>j初始化为空列表，其他情况初始化为[None]，画一个矩阵就可以看出来了。
        3.确定dp方程，求dp[i][j],以i-j之间数字为顶点的所有情况相加即可，
        例如，求dp[1][3]，分别以1,2,3为顶点，以1为顶点，左边值更大，右边值更小,
        左子树为dp[1][0]，右子树为dp[2][3]，两个树排列组合就可以,dp[1][0]为None,
        4.确定循环顺序，画矩阵可以看出来，从下向上进行循环，求dp[1][3]必须要知道dp[2][3]，
        求dp[2][4]必须要知道dp[3][4],dp[2][3]，
        5.写代码时候注意边界情况需要额外判断
        """
        if n == 0:
            return None
        # 对dp进行初始化
        dp = []
        for i in range(0, n+1):
            dp.append([])
            for j in range(0, n+1):
                if i == j:
                    dp[i].append([TreeNode(i)])
                elif i < j:
                    dp[i].append([])
                else:
                    dp[i].append([None])
        dp[0][0] = [None]
        for i in range(n - 1, 0, -1):  # 自下向上进行循环
            for j in range(i + 1, n + 1):
                for r in range(i, j + 1):  # i-j每一个节点为顶点的情况
                    left = r + 1 if r < j else r  # 右边的值需要边界判断，不然会溢出数组
                    for x in dp[i][r - 1]:  # 左右子树排列组合
                        for y in dp[left][j]:
                            node = TreeNode(r)
                            node.left = x
                            node.right = y
                            if r == j:
                                node.right = None
                            dp[i][j].append(node)  # dp[i][j]添加此次循环的值
        return dp[1][n]


solu = Solution()
ans = solu.generateTrees(3)
print(ans)



