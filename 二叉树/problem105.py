"""
105.从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历和中序遍历构造二叉树
注意：假设树中没有重复的元素
这是一道以前考研数据结构常常考的题，但不是敲代码而是画出该二叉树
通常前序遍历，中序遍历，后序遍历这三者，只要有一个中序遍历加上其他任意一个都是可以还原二叉树的
正好我们来熟悉这个过程的代码实现。由前序遍历和中序遍历输出后序遍历，由后序遍历和中序遍历输出前序遍历
同时还有一个层次遍历，层次遍历加上某一个遍历也可以还原这棵二叉树，我们都全部实现一遍吧
额外的实现部分放到code_template目录下，以中文名命名，以后想看的话好找一些。这里就实现该题的解答
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            node = stack[-1]
            preorderVal = preorder[i]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)
        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
solu = Solution()
root = solu.buildTree(preorder, inorder)
# 后序遍历验证一下
def post(root: TreeNode):
    if not root:
        return None
    if root.left:
        post(root.left)
    if root.right:
        post(root.right)
    print(root.val)

post(root)
