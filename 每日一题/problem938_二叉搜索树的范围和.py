class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # 直接遍历一遍也可以的。节点数目是四次方级别的，可以
        # 还是中序遍历非递归吧
        stack = []
        ans = 0

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            if stack:
                node = stack.pop()
                if low <= node.val <= high:
                    ans += node.val
                elif node.val > high:
                    break
                root = node.right
        return ans
