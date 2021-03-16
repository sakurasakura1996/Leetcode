"""
剑指 Offer 34. 二叉树中和为某一值的路径
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
提示：
节点总数 <= 10000
注意：本题与主站 113 题相同：
"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, summ: int) -> List[List[int]]:
        # 首先，二叉树的问题中，下面这句可以说是常规语句，直接写出来肯定对，就是判断是否为空
        if not root:
            return []
        ans = []
        # 采用回溯方法来写，
        def backtrace(node: TreeNode, cur: List[int], target: int):
            # node为访问到的节点， cur 为存储的路径列表，target为当前路径的和
            # 回溯法，首先先写递归的终止条件，那就是如果 node为叶子节点，且和等于summ，那么就把cur加入到ans中
            if not node.left and not node.right and target == summ:
                ans.append(cur)
                return
            if node.left:
                backtrace(node.left, cur+[node.left.val], target+node.left.val)
            if node.right:
                backtrace(node.right, cur+[node.right.val], target+node.right.val)
        backtrace(root, [root.val], root.val)
        return ans


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    solu = Solution()
    ans = solu.pathSum(root, 9)
    print(ans)


