"""
114. 二叉树展开为链表
给定一个二叉树，原地将它展开为一个单链表。
例如，给定二叉树
    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        # 递归方法
        preorderList = list()

        def preOrder(root:TreeNode):
            if root:
                preorderList.append(root)
                preOrder(root.left)
                preOrder(root.right)

        preOrder(root)
        size = len(preorderList)
        for i in range(1,size):
            prev, cur = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = cur

    def flatten_2(self, root: TreeNode) -> None:
        preorderList = list()
        stack = list()
        node = root

        while node or stack:
            while node:
                preorderList.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        size = len(preorderList)
        for i in range(1, size):
            prev, cur = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = cur
