"""
面试题68 - II. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
注意：本题与主站 236 题相同
"""
# 此题为II，相比I的话就是少了一个二叉搜索树的条件。
# 若root为p，q的最近公共祖先，则只可能为以下条件之一：
# 1.p和q在root的子树中，且分列root的两侧中
# 2.p=root，则q在root的左子树或右子树中
# 3.q=root，则p在root的左子树或右子树中
# 考虑通过递归对二叉树进行后续遍历，当遇到节点p或q时返回。从底至顶回溯，当节点p，q在节点root的两侧时，节点root即为最近公共祖先，则向上返回root
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root:TreeNode,p:TreeNode,q:TreeNode)-> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left:return right
        if not right:return left
        return root
