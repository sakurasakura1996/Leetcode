"""
872. 叶子相似的树
请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
提示：
给定的两颗树可能会有 1 到 200 个结点。
给定的两颗树上的值介于 0 到 200 之间。
"""

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
from collections import deque
class Solution:
    ans = []
    def levelOrder(self, root:TreeNode)->List[int]:
        # BFS 层次遍历一遍二叉树，然后把题中的 叶值序列 返回,不对，存在上一层先被存入ans数组中的情况。
        # if not root:
        #     return []
        # deq = deque()
        # deq.append(root)
        # ans = []
        # while deq:
        #     node = deq.popleft()
        #     if not node.left and not node.right:
        #         ans.append(node.val)
        #     if node.left:
        #         deq.append(node.left)
        #     if node.right:
        #         deq.append(node.right)
        # return ans
        if not root:
            return []
        if not root.left and not root.right:
            self.ans.append(root.val)
        if root.left:
            self.levelOrder(root.left)
        if root.right:
            self.levelOrder(root.right)
        return self.ans


    def leafSimilar(self, root1: TreeNode, root2: TreeNode)->bool:
        ans1 = self.levelOrder(root1).copy()
        # print(ans1)
        self.ans.clear()
        # print(ans1)
        ans2 = self.levelOrder(root2).copy() # 一定要记得copy()因为他们都在用self.ans来存储，而且copy()完成之后一定要清空啊。搞了半天
        print(ans2)
        return ans1 == ans2


root1 = TreeNode(1)
root2 = TreeNode(1)
solu = Solution()
ans = solu.leafSimilar(root1,root2)
print(ans)