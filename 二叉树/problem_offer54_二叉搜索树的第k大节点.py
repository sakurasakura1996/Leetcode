"""
给定一棵二叉搜索树，请找出其中第k大的节点。
示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
限制：1 ≤ k ≤ 二叉搜索树元素个数
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 第k大的节点，我们可以遍历一遍，把所有值放入到list中，然后排个序找到第k个值
# 上面的方法不是太好，因为他都没有用到这个二叉搜索树，普通二叉树也可以这样做
#
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        ans = []
        stack = [root]
        while stack:
            node = stack.pop(0)
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        ans.sort()   # 从小到大的顺序正序
        return ans[-k]

    def kthLargest_2(self, root: TreeNode, k:int) -> int:
        # 二叉搜索树有一个比较重要的性质：中序遍历的结果就是有序的
        def dfs(root):
            ans = []
            if not root:
                return ans
            if root.right:
                ans.extend(dfs(root.right))
            ans.append(root.val)
            if root.left:
                ans.extend(dfs(root.left))
            return ans
        ans = dfs(root)
        return ans[k-1]

