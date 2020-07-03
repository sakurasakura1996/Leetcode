"""
617.合并二叉树
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
示例 1:
输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。
"""
# 最先想到的有两种思路，一个是，两个树都层次遍历（BFS）一遍，然后存入数组中，加起来之后在构建二叉树
# 第二个思路就是两棵树同时遍历，在遍历过程中创建好返回的结果二叉树

from typing import List
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bfs_mergeTrees(self, t1: TreeNode, t2:TreeNode) -> TreeNode:
        # 层次遍历
        from collections import deque
        if not (t1 and t2): return t1 if not t2 else t2
        que = deque()
        que.append((t1, t2))
        while que:
            curleft, curright = que.popleft()
            curleft.val += curright.val  # 加和到左树
            if curleft.left and curright.left:  # 两树的当前节点的左子节点都存在
                que.append((curleft.left, curright.left))  # 则直接添加到队列中
                print(que)
            elif not curleft.left:  # 左树的左节点不存在时，
                curleft.left = curright.left  # 将右树的左节点移到左树的左节点
            if curleft.right and curright.right:  # 同理处理右节点
                que.append((curleft.right, curright.right))
            elif not curleft.right:
                curleft.right = curright.right
        return t1


    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 想了半天，发现还是递归好理解啊。
        if not t1:return t2
        if not t2:return t1
        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left,t2.left)
        root.right = self.mergeTrees(t1.right,t2.right)
        return root




