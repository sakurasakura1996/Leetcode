"""
404. 左叶子之和
计算给定二叉树的所有左叶子之和。
示例：
    3
   / \
  9  20
    /  \
   15   7
在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
"""
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            ans += root.left.val
        elif root.left:
            ans += self.sumOfLeftLeaves(root.left)
        if root.right:
            ans += self.sumOfLeftLeaves(root.right)
        return ans
