"""
530. 二叉搜索树的最小绝对差
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
示例：
输入：
   1
    \
     3
    /
   2
输出：
1
解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
提示：
树中至少有 2 个节点。
本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 中序遍历，然后不断更新ans吧
        import sys
        ans = sys.maxsize
        stack = []
        prev = -1
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                root = node.right
                if prev != -1:
                    ans = min(ans,node.val-prev)
                prev = node.val
        return ans
