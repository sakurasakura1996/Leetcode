"""
100. 相同的树
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
输出: true
示例 2:
输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]
输出: false
示例 3:
输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
输出: false
"""
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self,p:TreeNode,q:TreeNode)->bool:
        # 递归解法
        if not p:
            return not q
        if not q:
            return not p
        if p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True
        return False

    def isSameTree_2(self,p:TreeNode,q:TreeNode)->bool:
        # 迭代解法
        from collections import deque

        def check(p,q):
            if not p:return not q
            if not q:return not p
            if p.val == q.val:
                return True
            return False

        deq = deque()
        deq.append((p,q))
        while deq:
            p,q = deq.popleft()
            if not check(p,q):
                return False
            if p:
                deq.append((p.left,q.left))
                deq.append((p.right,q.right))
        return True