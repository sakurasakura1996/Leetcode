"""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 这种问题，递归方法都是可以解决滴
        # 但是下面的方法是错的，我们一定要小心啊，下面代码错在哪里呢，比如根节点为5，但是右节点为6，但是右节点的左节点值为4，下面的代码
        # 判断这棵二叉树是二叉搜索树，这就是没有考虑清楚二叉搜索树的特征，节点的右子树只包含大于当前节点的数，我们只在意了右节点，而没有关注其他的。
        if not root:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def isValidBST2(self, root: TreeNode) -> bool:
        # 那么正确的递归方法应该怎么写呢
        def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

    def isValidBST3(self, root: TreeNode) -> bool:
        # 后者中序遍历一下，看是不是有序的,这个解法还是太蠢了啊

        def inOrder(root: TreeNode):
            if not root:
                return []
            ans = []
            if root.left:
                tmp = inOrder(root.left)
                ans.extend(tmp.copy())
            ans.append(root.val)
            if root.right:
                tmp = inOrder(root.right)
                ans.extend(tmp.copy())
            return ans

        if not root:
            return True
        ans = inOrder(root)
        for i in range(1, len(ans)):
            if ans[i] <= ans[i-1]:
                return False
        return True






if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.right.left =TreeNode(3)
    root.right.right = TreeNode(7)
    ans = solu.isValidBST2(root)
    print(ans)
