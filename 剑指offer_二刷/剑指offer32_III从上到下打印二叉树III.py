"""
剑指 Offer 32 - III. 从上到下打印二叉树 III
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [20,9],
  [15,7]
]
提示：
节点总数 <= 1000
"""
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        queue = deque()
        queue.append(root)
        ans.append([root.val])
        tmp = []
        tmp_value = []
        i = 0
        while queue:
            node = queue.popleft()
            if node.left:
                tmp.append(node.left)
                tmp_value.append(node.left.val)
            if node.right:
                tmp.append(node.right)
                tmp_value.append(node.right.val)
            if not queue and tmp:
                if i % 2 == 0:
                    ans.append(list(reversed(tmp_value.copy())))
                else:
                    ans.append(tmp_value.copy())
                tmp_value = []
                queue.extend(tmp.copy())
                tmp = []
                i += 1
        return ans
# 总感觉我上面的https://iotsakura.top/


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solu = Solution()
    ans = solu.levelOrder(root)
    print(ans)