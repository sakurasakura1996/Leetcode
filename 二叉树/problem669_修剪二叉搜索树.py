"""
669. 修剪二叉搜索树
给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。
你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
示例 1:
输入:
    1
   / \
  0   2

  L = 1
  R = 2
输出:
    1
      \
       2
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        if L <= root.val <= R:
            if root.left:
                root.left = self.trimBST(root.left,L,R)
            else:
                root.left = None
            # 其实这里的判断是没啥必要的，我只需要递归调用函数就行了，因为函数中已经有判断是否该节点为空的语句
            if root.right:
                root.right = self.trimBST(root.right,L,R)
            else:
                root.right = None
            return root
        elif root.val < L:
            return self.trimBST(root.right,L,R)
        else:
            return self.trimBST(root.left,L,R)
# 这道题的递归方法我还是写了很久才写对的，

