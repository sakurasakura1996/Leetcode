"""
538. 把二叉搜索树转换为累加树
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
例如：
输入: 原始二叉搜索树:
              5
            /   \
           2     13
输出: 转换为累加树:
             18
            /   \
          20     13

注意：本题和 1038: https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同
"""
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

# 只要是二叉搜索树，那么有序的性质就一定要注意要用到，如果题目改成每个节点的值都是原来的节点值
# 加上所有小于它的节点值之和，那么可能大家都会想到能不能用中序遍历，然后一直加。
# 那么现在题目反过来了，其实问题也不大啊，我们用倒后序遍历看看行不行。
class Solution:

    def convertBST(self, root:TreeNode) -> TreeNode:
        # 逆中序遍历的非递归实现
        stack = []
        ans = root
        num = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.right
            if stack:
                node = stack.pop()
                root = node.left
                node.val += num
                num = node.val
        return ans

