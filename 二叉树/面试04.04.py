"""
面试04.04 检查平衡性
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。
示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def treeHeight(self, node:TreeNode)-> int:
        if not node:
            return 0
        else:
            left_height = self.treeHeight(node.left)
            right_height = self.treeHeight(node.right)
            if abs(left_height - right_height) > 1 or left_height == -1 or right_height == -1:
                return -1
            else:
                return 1+max(left_height, right_height)

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        root_height = self.treeHeight(root)
        if root_height == -1:
            return False
        return True

solu = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
ans = solu.isBalanced(root)
print(ans)



