class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return ans

        def backtrace(root):
            nonlocal ans
            if not root.left and not root.right:
                ans += root.val
                return
            if root.left:
                root.left.val += (root.val * 10)
                backtrace(root.left)
            if root.right:
                root.right.val += (root.val * 10)
                backtrace(root.right)

        backtrace(root)
        return ans

if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    ans = solu.sumNumbers(root)
    print(ans)