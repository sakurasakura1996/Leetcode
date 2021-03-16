from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 运用递归和迭代两种方法来解决
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def check(root1, root2):
            if not root1:
                return not root2
            if not root2:
                return not root1
            if root1.val != root2.val:
                return False
            return check(root1.left, root2.right) and check(root1.right, root2.left)

        ans = check(root.left, root.right)
        return ans

    def isSymmetric2(self, root: TreeNode) -> bool:
        # 迭代方法实现,首先想到的是用层次遍历，然后每一层看是否对称
        if not root:
            return True

        queue = [root.left, root.right]
        while queue:
            left = queue.pop()
            right = queue.pop()

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True


