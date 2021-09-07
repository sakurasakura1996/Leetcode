class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # 因为这棵树是二叉搜索树，所以中序遍历是有序的
        if not root:
            return None
        # 回顾下中序遍历非递归方法。
        stack = []
        ans = float('inf')
        pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                if pre == None:
                    pre = root.val
                else:
                    ans = min(ans, abs(root.val - pre))
                    pre = root.val
                root = root.right
        return ans


if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(48)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(49)
    ans = solu.minDiffInBST(root)
    print(ans)
