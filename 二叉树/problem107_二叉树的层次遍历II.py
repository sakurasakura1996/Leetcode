"""
107. 二叉树的层次遍历 II
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：
[
  [15,7],
  [9,20],
  [3]
]
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 之前做了一个题目，和这个题目很像，只不过输出的顺序是从上到下的，那么这题其实也很简单，按原来的思路直接倒序一下不就行了
from typing import List
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = deque()
        que.append(root)
        ans = []
        level_value = []
        node_level = []
        while que:
            node = que.popleft()
            level_value.append(node.val)

            if node.left:
                node_level.append(node.left)
            if node.right:
                node_level.append(node.right)

            if not que:
                level = level_value.copy()
                ans.insert(0,level)
                que.extend(node_level)
                level_value.clear()
                node_level.clear()
        return ans



