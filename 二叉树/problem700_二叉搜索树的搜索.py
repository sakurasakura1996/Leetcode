"""
700.二叉搜索树中的搜索
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
例如，
给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3
和值: 2
你应该返回如下子树:

      2
     / \
    1   3
在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 此类关于树的简单题，大多递归都是可以解决的
        if not root:
            return None
        if root.val == val:
            return root
        if root.val < val:
            ans = self.searchBST(root.right, val)
        if root.val > val:
            ans = self.searchBST(root.left, val)
        return ans

    def searchBST_2(self, root:TreeNode, val:int) -> TreeNode:
        # 尝试使用非递归方法来做一做
        stack = [root]
        while stack:
            tmp = stack.pop()
            if tmp == None:
                continue
            if tmp.val == val:
                return tmp
            else:
                stack.append(tmp.left)
                stack.append(tmp.right)
        return None

    def searchBST_3(self, root:TreeNode, val:int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None



