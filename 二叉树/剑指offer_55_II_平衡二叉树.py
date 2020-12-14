"""
剑指 Offer 55 - II. 平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
限制：
1 <= 树的结点个数 <= 10000
注意：本题与主站 110 题相同
"""
# 记录每个节点作为根节点的树的高度
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

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        if abs(left_depth-right_depth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False






















