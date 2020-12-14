"""
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def dfs(root:TreeNode)->int:
            # 从当前节点root到叶节点的最小深度
            if not root:
                return 0
            if root.left and root.right:
                return min(dfs(root.left), dfs(root.right))+1
            elif root.left:
                return dfs(root.left) + 1
            elif root.right:
                return dfs(root.right) + 1
            else:
                return 1

        return dfs(root)

    def minDepth_2(self, root:TreeNode)->int:
        # 少用递归，多用栈等数据结构来写迭代方法  DFS
        if not root:
            return 0
        stack, ans = [(1,root)], float('inf')

        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                ans = min(ans, depth)
            for c in children:
                if c:
                    stack.append((1+depth,c))
        return ans

    def minDepth_3(self, root:TreeNode) -> int:
        # BFS
        from collections import deque
        if not root:
            return 0
        qeque = deque()
        qeque.append((1,root))

        while qeque:
            depth, node = qeque.popleft()
            children = [node.left, node.right]
            if not any(children):
                return depth
            for c in children:
                if c:  # 这里判断c不为空很重要，不然会报错
                    qeque.append((1+depth,c))


