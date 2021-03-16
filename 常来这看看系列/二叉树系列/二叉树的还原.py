"""
这个系列以前也写过一次，主要还是代码功底差，忘得太快了，这里再自己推导一次。
前序+中序，后序+中序，反正必须要有中序顺序，我们就可以还原出这颗二叉树
"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 根据某二叉树的前序遍历和中序遍历还原这棵二叉树。因为树中元素不相同，所以不断找到根节点在中序遍历中的位置
        if not preorder:
            return
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 上面的空间复杂度其实还可以简化，我们并没有改动preorder和inorder这两个list，但是每次递归调用
        # 我们都重新创建一个复制的部分list，太浪费，可以用索引来标记
        def build(preleft: int, preright: int, inleft: int, inright: int) -> TreeNode:
            if preleft > preright:
                return
            root = TreeNode(preorder[preleft])
            idx = inorder.index(preorder[preleft])
            root.left = build(preleft+1, preleft+idx-inleft, inleft, idx-1)
            root.right = build(preleft+idx-inleft+1, preright, idx+1, inright)
            return root

        n = len(preorder)
        root = build(0, n - 1, 0, n - 1)
        return root

    def buildTree3(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 根据中序遍历和后序遍历还原二叉树，大致思路和前面差不多
        if not inorder:
            return
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left = self.buildTree3(inorder[:idx], postorder[:idx])
        root.right = self.buildTree3(inorder[idx+1:], postorder[idx:-1])
        return root









