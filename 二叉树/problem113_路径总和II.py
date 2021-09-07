from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # 注意看清楚题目哦，这里要找的路径是 从 根节点 到 叶子节点路径总和等于i给定目标和的路径。
        if not root:
            return []
        ans = []


        def backtrace(cur, node, summ):
            if summ == targetSum and not node.left and not node.right:
                ans.append(cur.copy())
                return
            if node.left:
                cur.append(node.left.val)
                summ += node.left.val
                backtrace(cur, node.left, summ)
                cur.pop()
                summ -= node.left.val
            if node.right:
                cur.append(node.right.val)
                summ += node.right.val
                backtrace(cur, node.right, summ)
                cur.pop()
                summ -= node.right.val

        backtrace([root.val], root, root.val)
        return ans


if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    ans = solu.pathSum(root, 22)
    print(ans)