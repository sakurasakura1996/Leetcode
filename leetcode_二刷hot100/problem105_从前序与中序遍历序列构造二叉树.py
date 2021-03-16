from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 有中序遍历加另外一个遍历基本上都能还原这颗二叉树
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 此种写法比较浪费内存，因为我们每次都拷贝了preorder和inorder数组
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
        return root
