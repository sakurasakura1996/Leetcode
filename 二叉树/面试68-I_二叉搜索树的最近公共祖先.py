"""
面试题68 - I. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
示例 1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
说明:
*所有节点的值都是唯一的。
*p、q 为不同节点且均存在于给定的二叉搜索树中。
注意：本题与主站 235 题相同
"""
# 解题思路：
# 祖先的定义： 若节点 p 在节点 root 的左（右）子树中，或 p=root，则称 root 是 p 的祖先。
# 最近公共祖先的定义： 设节点 root 为节点 p,q 的某公共祖先，若其左子节点 root.left 和右子节点 root.right 都不是 p,q 的公共祖先，
# 则称 root 是 “最近的公共祖先” 。
# 根据以上定义，若 root 是 p,q 的 最近公共祖先 ，则只可能为以下情况之一：
# p 和 q 在 root 的子树中，且分列 root 的 异侧（即分别在左、右子树中）；
# p=root，且 q 在 root 的左或右子树中；
# q=root，且 p 在 root 的左或右子树中；
# 本题给了两个重要条件：
# 1.树为二叉搜索树  2.树的所有节点的值都是唯一的，根据以上条件可以方便地判断p，q与root的子树关系，即
# 若 root.val < p.val,则p在root右子树中  # 我擦，我感觉我搞忘了这是一棵二叉搜索树了，有大小关系的。
# 若 root.val > p.val，则p在root左子树中
# 若 root.val = p.val,则p和root指向同一节点
# 可以使用递归和迭代两种方法求解
class TreeNode:
    def __init(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root:TreeNode, p:TreeNode, q:TreeNode)-> TreeNode:
        # 递归方法
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        # if root.val == p.val or root.val == q.val or p.val < root.val < q.val or q.val < root.val < p.val:
        #     return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root

    def lowestCommonAncestor_2(self, root:TreeNode,p:TreeNode,q:TreeNode) -> TreeNode:
        # 使用迭代方法。循环搜索，当节点root为空时跳出
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            if root.val > p.val and root.val > q.val:
                root = root.left
            else:
                break
        return root






