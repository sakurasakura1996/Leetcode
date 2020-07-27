"""
637. 二叉树的层平均值
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
示例 1：
输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
提示：
节点值的范围在32位有符号整数范围内。
"""
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
from collections import deque
class Solution:
    def averageOfLevels(self, root:TreeNode) -> List[float]:
        if not root:
            return []
        que = deque()
        que.append(root)
        ans = []

        node_level = []
        value_level = []
        while que:
            node = que.popleft()
            value_level.append(node.val)

            if node.left:
                node_level.append(node.left)
            if node.right:
                node_level.append(node.right)
            if not que:
                average = sum(value_level) / len(value_level)
                ans.append(average)
                que.extend(node_level)
                node_level.clear()
                value_level.clear()
        return ans

