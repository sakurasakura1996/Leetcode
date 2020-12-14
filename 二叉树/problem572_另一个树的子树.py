"""
572. 另一个树的子树
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。
s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。
示例 1:
给定的树 s:
     3
    / \
   4   5
  / \
 1   2
给定的树 t：
   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：
     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：
   4
  / \
 1   2
返回 false。
"""
# 这道题和剑指offer26_树的子结构有点不太一样，那道题是只要子树部分相同即可，而不用管是否子树中还有多余的
# 而这道题需要判断的是两棵树是否有相同的子树，所以从子树根节点到叶节点必须都是相同的
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def check(self, A: TreeNode, B: TreeNode):
        if not A:
            return not B
        if not B:
            return not B
        return A.val == B.val and self.check(A.left, B.left) and self.check(A.right,B.right)


    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return not t
        if not t:
            return not s
        return self.check(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)




