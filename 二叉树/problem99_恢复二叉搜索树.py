""""
99. 恢复二叉搜索树
二叉搜索树中的两个节点被错误地交换。
请在不改变其结构的情况下，恢复这棵树。

示例 1:
输入: [1,3,null,null,2]
   1
  /
 3
  \
   2
输出: [3,1,null,null,2]

   3
  /
 1
  \
   2

例 2:
输入: [3,1,4,null,null,2]
  3
 / \
1   4
   /
  2
输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

  进阶:
使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        arr = [None, None, None]  # prev, first, second

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if arr[0] and node.val < arr[0].val:
                if not arr[1]:
                    arr[1] = arr[0]
                arr[2] = node
            arr[0] = node
            dfs(node.right)

        dfs(root)
        arr[1].val, arr[2].val = arr[2].val, arr[1].val
