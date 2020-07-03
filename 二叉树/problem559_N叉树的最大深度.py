"""
559.N叉树的最大深度
给定一个 N 叉树，找到其最大深度。
最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
例如，给定一个 3叉树 :
我们应返回其最大深度，3。
说明:
树的深度不会超过 1000。
树的节点总不会超过 5000。
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # 首先我觉得，要找到最大深度，最起码你所有的节点都会遍历一遍，那么基本上几种遍历方法都行
        if not root:
            return 0
        ans = 0
        for child in root.children:
            cur_max = self.maxDepth(child)
            ans = max(ans, cur_max)
        return ans+1
    # 还有方法，就是用迭代法，使用栈来替换递归策略。
    # 具体代码参考problem104，二叉树的最大深度，思路是一样的
