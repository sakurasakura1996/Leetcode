"""
653. 两数之和 IV - 输入 BST
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
案例 1:
输入:
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
输出: True

案例 2:
输入:
    5
   / \
  3   6
 / \   \
2   4   7
Target = 28
输出: False
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        def inOrder(root:TreeNode) -> List[int]:
            if not root:
                return []
            return inOrder(root.left) + [root.val] + inOrder(root.right)

        arr = inOrder(root)
        left = 0
        right = len(arr) - 1
        while left < right:
            num = arr[left] + arr[right]
            if num == k:
                return True
            elif num > k:
                right -= 1
            else:
                left += 1
        return False




