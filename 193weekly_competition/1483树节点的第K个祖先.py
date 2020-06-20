"""
给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。
请你设计并实现 getKthAncestor(int node, int k) 函数，函数返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。
树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。

"""
# from typing import List
# class TreeAncestor:
#
#     def __init__(self, n: int, parent: List[int]):
#         self.parent = parent
#         self.n = n
#
#
#     def getKthAncestor(self, node: int, k: int) -> int:
#         ans = node
#         while k!=0:
#             if ans == -1:
#                 return -1
#             ans = self.parent[ans]
#             k -= 1
#         return ans

# 好像这样写并没有什么问题，问题就出在效率太慢了。题目说查询次数小于5万次
# 而我们每一次查询都要从node节点从头开始往上查。那么，我就想到是否可以用
# 动态规划的方式去做呢，我们把每个node的父节点全部存下来，那么查询实现的复杂度
# 就可以达到O（1）了呢。只不过这个空间复杂度增加了。

from typing import List
import numpy as np
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.dp = list(-1*np.ones((n, n),dtype=np.int))
        for i in range(1, n):
            ans = i
            m = 0
            self.dp[i][0] = ans
            while ans != -1:
                ans = parent[ans]
                m += 1
                self.dp[i][m] = ans

    def getKthAncestor(self, node: int, k: int) -> int:
        if k >= len(self.dp):
            return -1
        return int(self.dp[node][k])

# 妈的，再出错调试了几次之后，上面的代码应该是没问题的了，但是还是超时了。
# 这特么就很尴尬了呀。
# 题解算法：采用DP倍增法，主要难度在于为什么会想到dp[node][j]表示的是node节点第2^j个祖先节点。
# 大概和这个树结构有点关系。
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.cols = 20      # log(50000) < 20

        self.dp = [[-1] * self.cols for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]
        # 动态规划设置祖先, dp[node][j] 表示 node 往前推第 2^j 个祖先
        for j in range(1, self.cols):
            for i in range(n):
                if self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
        return

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.cols - 1, -1, -1):   # 不是，这部分的寻找答案也太难懂了吧
            if k & (1 << i):   # & 和 << 都是二进制的位运算，&是按位与运算， << 是移位运算
                node = self.dp[node][i]
                if node == -1:
                    break
        return node

# 这道题还是可以多想想啊，看到一个大佬用到了DFS+层次遍历+二分查找，思路倒是比上面的好理解太多。
# 预备知识
# 一个节点的所有祖先节点(从根节点到该节点的路径上经过的所有点))的dfs序(从根节点已dfs访问的顺序)都在该节点前。
# 例如：
#
# dfs序为 0, 1, 3, 4, 2, 5, 6。每个节点的祖先节点都在它前面。
# 可以通过BFS对树进行层次遍历，确定每层有哪些节点。
# 分析
# 有了上面两个预备知识，我们可以想到：
# 假设要找节点A的第k个父节点，节点A在第L层，即只需找到第L-k层的所有节点中A的祖先节点。
# 又由于A的祖先节点在每一层只有一个，且dfs序必然在节点A前，所以可以通过二分查找在第L-k层中找比A小且距离A最近的元素即为答案。
# 后续练习练习 DFS 和 BFS再来做做这题这个方法。

# Your TreeAncestor object will be instantiated and called as such:
n = 7
parent = [-1,0,0,1,1,2,2]
obj = TreeAncestor(n, parent)
param_1 = obj.getKthAncestor(6, 1)
print(param_1)
print(type(param_1))