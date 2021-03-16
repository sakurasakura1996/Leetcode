"""
543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
注意：两结点之间的路径长度是以它们之间边的数目表示。
"""
from functools import lru_cache
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 采用递归的方法，分别计算每个节点左右支路中的最大距离，然后加起来，找到其中的最大值
class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def path(node: TreeNode) -> int:
            # 用于计算某节点到叶节点的左右
            if not node:
                return 0
            L = path(node.left)
            R = path(node.right)
            self.ans = max(self.ans, L+R)
            return max(L, R)+1
        path(root)

        return self.ans
