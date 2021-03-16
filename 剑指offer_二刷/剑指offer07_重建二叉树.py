"""
剑指 Offer 07. 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

限制：
0 <= 节点个数 <= 5000
注意：本题与主站 105 题重复
"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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
        