"""
106.从中序与后序遍历序列构造二叉树
你可以假设树中没有重复的元素
上一题105题是由前序中序构造二叉树，思维方法很类似啦。都可以在code_template中找到模板代码和思维过程。
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        root_idx = inorder.index(root.val)
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx+1:], postorder[root_idx:-1])
        return root