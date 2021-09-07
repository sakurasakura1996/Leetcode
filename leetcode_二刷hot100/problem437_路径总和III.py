from functools import lru_cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 1
    @lru_cache(None)
    def pathSum(self, root: TreeNode, summ: int) -> int:
        if not root:
            return 0
        if root.val == summ:
           self.ans += 1
        if not root.left and not root.right:
            return 0
        # 路径不包含root节点：
        # 这个代码是有问题的，上次做这道题的时候就是这样的想法，错在哪里呢，我们还是没有搞清楚函数的定义。
        # 下面的情况，如果我们选择了root节点作为路径节点，那么递归下去，如果我们又没选root的子节点，但是还可以继续递归下去，那岂不是多了很多
        # 总结来说，我下面的代码没有考虑到路径的连续性啊。
        self.pathSum(root.left, summ)
        self.pathSum(root.right, summ)
        self.pathSum(root.left, summ-root.val)
        self.pathSum(root.right, summ-root.val)

    def pathSum2(self, root: TreeNode, summ: int) -> int:

        @lru_cache(None)
        def count_path(root: TreeNode, target: int) -> int:
            # 我们要考虑清楚每一个函数的定义，count_path返回的是，以root节点为路径开始节点，然后路径只能向下，终点可以不是叶节点
            # 然后路径和为target的路径数目
            if not root:
                return 0
            if root.val == target:
                return 1 + count_path(root.left, target-root.val) + count_path(root.right, target-root.val)
            else:
                return count_path(root.left, target-root.val) + count_path(root.right, target-root.val)

        if not root:
            return 0
        return count_path(root, summ) + self.pathSum2(root.left, summ) + self.pathSum2(root.right, summ)

