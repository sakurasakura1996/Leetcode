"""
965. 单值二叉树
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回 true；否则返回 false。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # 遍历一下二叉树，比较下即可
        value = root.val
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            if node.val != value:
                return False
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return True

    def isUnivalTree_2(self, root: TreeNode) -> bool:
        # 用递归方法来写
        left_correct = (not root.left or root.val == root.left.val and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val and self.isUnivalTree(root.right))
        return left_correct and right_correct

