"""
给你二叉树的根节点 root 和一个整数 distance 。

如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。

返回树中 好叶子节点对的数量 。
输入：root = [1,2,3,null,4], distance = 3
输出：1
解释：树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。
提示：

tree 的节点数在 [1, 2^10] 范围内。
每个节点的值都在 [1, 100] 之间。
1 <= distance <= 10
"""
# 感觉这类题目用DFS基本上是都可以解决的，但是自己还是不够熟悉。
# 解题思路
# 1.遍历这棵树，对于每一个遍历到的节点node，计算node左右子树中叶子节点到node的距离，记录在dict中。
# 2.组合左右子树中的叶子节点对，如果它们的距离只和小于distance，则结果加1。
# 3.向上返回当前节点node的所有叶子节点距离给上层节点。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ans = 0
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root or not root.left and not root.right:
            return 0

        def _dfs(root):
            """获取左右子树中叶子节点到当前节点的距离,记录在dict中"""
            if not root:
                return {}
            # 叶子节点
            if not root.left and not root.right:
                return {root:0}

            left_leaf = _dfs(root.left)
            right_leaf = _dfs(root.right)
            # 距离加1
            for k, v in left_leaf.items(): left_leaf[k] = v+1
            for k, v in right_leaf.items(): right_leaf[k] = v+1

            for lk, lv in left_leaf.items():
                for rk, rv in right_leaf.items():
                    if lv + rv <= distance:
                        self.ans += 1

            # 合并左右子树的叶子节点，向上返回
            left_leaf.update(right_leaf)
            return left_leaf

        _dfs(root)
        return self.ans




