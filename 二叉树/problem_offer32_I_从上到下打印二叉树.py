"""
剑指 Offer 32 - I. 从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回：
[3,9,20,15,7]
"""
from typing import List
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        # 这就是二叉树的层次遍历或者说是BFS
        if not root:
            return []

        ans = []
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            ans.append(node.val)
        return ans

    # 看到题解中有一个很好的提示，他说的是我们python中一般使用队列时就是直接用了list列表来实现，那么pop(0)的时间复杂度为O(N)
    # 如果使用 collections中的双端队列deque(),其popleft()方法可达到O(1)的时间复杂度。这样更高效一点
    def levelOrder_2(self, root: TreeNode) -> List[int]:
        # using collections's deque
        from collections import deque
        if not root:
            return []
        ans = []
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            ans.append(node.val)
        return ans

