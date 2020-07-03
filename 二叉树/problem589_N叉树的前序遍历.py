"""
给定一个N叉树，返回其节点值的前序遍历
"""
from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # 递归方法求解
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        ans.append(root.val)
        for child in root.children:
            ans.extend(self.preorder(child))
        return ans

    def preorder_2(self, root: Node) -> List[int]:
        # 非递归方法的实现，肯定要用栈来记录
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        return ans

