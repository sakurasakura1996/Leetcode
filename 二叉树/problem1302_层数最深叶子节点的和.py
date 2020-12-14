"""
1302. 层数最深叶子节点的和
给你一棵二叉树，请你返回层数最深的叶子节点的和。
示例
输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15
提示：
树中节点数目在 1 到 10^4 之间。
每个节点的值在 1 到 100 之间。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# BFS must can solve the problem,but may not be a good solution
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return 0
        from collections import deque
        stack = deque()
        stack.append(root)
        nextlevel = []
        ans = 0
        while stack:
            node = stack.popleft()
            if node.left:
                nextlevel.append(node.left)

            if node.right:
                nextlevel.append(node.right)

            ans += node.val
            if not stack and nextlevel:
                ans = 0
                stack.extend(nextlevel.copy())
                nextlevel.clear()

        return ans

