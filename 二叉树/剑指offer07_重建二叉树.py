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
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder:List[int],inorder:List[int]) -> TreeNode:
        if not preorder:
            return None
        tree_len = len(preorder)
        if tree_len == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        # 接下来如果想递归的话，中序遍历的数组还比较好分开，前序遍历的数组就要分出根节点的左右子树部分来，另外假设树是没有重复元素的
        root_idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
        # 注意这里的数组取值如果冒号后面写-1的话最后一个值没有取到，直接省略就可以了
        return root
