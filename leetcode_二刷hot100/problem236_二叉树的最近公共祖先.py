class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 这道题没有搞出来，有点不应该啊，还是可以通过递归来解决问题啊
"""
根据以上定义，若 root 是 p,q 的 最近公共祖先 ，则只可能为以下情况之一：
    1.p 和 q 在 root 的子树中，且分列 root 的 异侧（即分别在左、右子树中）；
    2.p=root ，且 q 在 root 的左或右子树中；
    3.q=root ，且 p 在 root 的左或右子树中；

作者：jyd
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        # 这道题递归要想清楚递归的终止条件
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # if not left:
        #     return right
        # if not right:
        #     return left
        # return root
        # 便于理解，理清思路如下：
        if not left and not right:
            return
        if not left:
            return right
        if not right:
            return left
        return root