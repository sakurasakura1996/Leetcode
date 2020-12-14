"""
剑指 Offer 32 - III. 从上到下打印二叉树 III
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
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
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root:TreeNode)->List[List[int]]:

        ans = []
        if not root:
            return []
        stack = [root]
        next_level = []
        next_level_value = []
        ans.append([root.val])
        i = 1
        while stack:
            node = stack.pop(0)
            if node.left:
                next_level.append(node.left)
                next_level_value.append(node.left.val)
            if node.right:
                next_level.append(node.right)
                next_level_value.append(node.right.val)
            if not stack and next_level:
                stack.extend(next_level)
                # ans.append(next_level_value)  后面next_level_value会清空，这样写，一旦后面清空，这里共享内存的内容也会清空了
                # value = next_level_value.copy() # 避免直接加入共享内存会删除结果
                if i%2==1:
                    ans.append(next_level_value.copy()[::-1])
                else:
                    ans.append(next_level_value.copy())
                next_level.clear()
                next_level_value.clear()
                i += 1
        return ans


solu = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left =TreeNode(4)
root.right.right = TreeNode(5)
ans = solu.levelOrder(root)
print(ans)
