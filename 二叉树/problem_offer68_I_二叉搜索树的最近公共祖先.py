"""
剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
示例 1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中
此题与主站235题相同
"""
# 最近公共祖先问题，这个问题还是比较经典的。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 但是我好像写不出来，这就有点特么尴尬了。
class Solution:
    def lowestCommonAncestor(self, root:TreeNode,p:TreeNode,q:TreeNode)->TreeNode:
