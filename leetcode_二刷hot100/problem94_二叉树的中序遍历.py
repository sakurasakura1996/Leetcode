from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归

        if not root:
             return []
        if root.left:
            self.inorderTraversal(root.left)
        self.ans.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        return self.ans

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        # 迭代法
        stack = []
        ans = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                ans.append(node.val)
                if node.right:
                    root = node.right
        return ans


if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    ans = solu.inorderTraversal2(root)
    print(ans)


