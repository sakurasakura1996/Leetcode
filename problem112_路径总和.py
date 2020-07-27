"""
112.路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。
示例: 
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# BFS 或者 DFS应该都可以实现。
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            if node.left:
                node.left.val += node.val
                que.append(node.left)
            if node.right:
                node.right.val += node.val
                que.append(node.right)
            if not node.left and not node.right and node.val == sum:
                return True
        return False

    def hasPathSum_2(self, root: TreeNode, sum:int) -> bool:
        # 题解中说到了用递归，那就用一下吧
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum_2(root.left, sum-root.val) or self.hasPathSum_2(root.right, sum-root.val)



