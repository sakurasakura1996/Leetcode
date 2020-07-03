"""
104.二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    def maxDepth_2(self, root:TreeNode) -> int:
        # 采用非递归方法来做

        if not root:
            return 0
        stack = [(1,root)]
        depth = 0
        while stack:
            current_depth, node = stack.pop(0)
            if node:
                depth = max(depth, current_depth)
                stack.append((current_depth+1, node.left))
                stack.append((current_depth+1, node.right))
        return depth
