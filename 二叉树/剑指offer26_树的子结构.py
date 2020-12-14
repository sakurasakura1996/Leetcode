"""
剑指 Offer 26. 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。
例如:
给定的树 A:
     3
    / \
   4   5
  / \
 1   2
给定的树 B：
   4
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：
0 <= 节点个数 <= 10000
类似的题目还有572，1367，101
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def check(self, s, t):
        if not t:   # 这里要想好，为什么t为空的时候返回True。因为我们的要求是匹配子结构啊，如果s左子树不为空，而t的左子树已经是空了，那也匹配啊
            return True
        if not s:
            return False
        return s.val == t.val and self.check(s.left, t.left) and self.check(s.right, t.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:  # 如果A为空，B不管怎么样，结果都是False
            return False
        return self.check(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
