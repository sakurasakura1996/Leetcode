""""
面试27。二叉树的镜像
输入一个二叉树，输出它的镜像
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# way1 递归方法
# class Solution:
#     def mirrorTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return root
#         left_node = self.mirrorTree(root.left)
#         right_node = self.mirrorTree(root.right)
#         root.left = right_node
#         root.right = left_node
#         return root

# way2 栈方法
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root
