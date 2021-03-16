from functools import lru_cache
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 我们在用递归解决问题的时候，还是要搞清楚每个函数的实际含义啊。。。
# 我现在理解的函数的定义就是：返回以root节点为根节点的二叉树中的路径长度最大值，那么递归该函数的话，求得的就是以其子节点为根节点的二叉树中最大路径
# 那么原理上仅仅这一个函数不太好实现递归。还要定义一个从根节点到子节点的路径最大值函数，这样通过比较才能实现最大值。

class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        @lru_cache(None)
        def path(root: TreeNode):
            # 计算root节点到叶节点的最大路径长度
            if not root:
                return 0
            left = path(root.left)+1 if root.left else 0
            right = path(root.right)+1 if root.right else 0
            return max(left, right)

        if not root:
            return 0

        l = path(root.left)+1 if root.left else 0
        r = path(root.right)+1 if root.right else 0
        return max(l+r, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    def diameterOfBinaryTree2(self, root: TreeNode) -> int:
        self.ans = 1  # 记录节点个数，那么路径长度就等于 节点个数-1,总体思路上和上面自己写的差不多，但是代码和思路简洁了很多
        def depth(node):
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            self.ans = max(self.ans, l+r+1)
            # 返回以该节点为根的子树的深度
            return max(l, r) + 1     # 发现没有，一个函数其实实现了两个操作，一个是用ans来记录最大路径中的节点个数，一个用来返回子树深度

        depth(root)
        return self.ans - 1


if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.left.left.left.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
    root.left.right.right.right = TreeNode(9)
    ans = solu.diameterOfBinaryTree(root)
    print(ans)








