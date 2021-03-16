class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类 the root of binary tree
# @return int整型二维数组
#
class Solution:

    def threeOrders(self, root):
        self.pre_order = list()
        self.in_order = list()
        self.post_order = list()
        self.preOrder(root)
        self.inOrder(root)
        self.postOrder(root)
        return list([self.pre_order, self.in_order, self.post_order])

    def preOrder(self, root):
        if not root:
            return
        self.pre_order.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.in_order.append(root.val)
        self.inOrder(root.right)

    def postOrder(self, root):
        if not root:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        self.post_order.append(root.val)

        # write code here

if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    ans = solu.threeOrders(root)
    print(ans)