class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # 用中序遍历非递归方法来做, 感觉中序遍历非递归方法又不熟练了呀。。。
        stack = []
        pre = TreeNode(0)
        cur = pre
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                cur.right = node
                cur = node
                root = node.right
        return pre.right


if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    root.right.right = TreeNode(8)
    root.right.right.left = TreeNode(7)
    root.right.right.right = TreeNode(9)
    ans = solu.increasingBST(root)
    while ans:
        print(ans.val)
        ans = ans.right

