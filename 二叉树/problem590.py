"""
590.N叉树的后序遍历
给定一个N叉树，返回其节点值的后序遍历
"""
from typing import List


class Node:

    def __init__(self,val=None,children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        for child in root.children:
            if child:
                ans.extend(self.postorder(child))
        ans.append(root.val)
        return ans

    def postorder_2(self, root:Node)-> List[int]:
        # 采用迭代方法来写，这种编码方法应该多想多熟悉一些。N叉树后序遍历的非递归实现和二叉树原理应该相同的，具体参考code_template
        if not root:
            return []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop(0)
            for child in node.children:
                stack.append(child)
            ans.append(node.val)
        return reversed(ans)


