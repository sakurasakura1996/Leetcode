class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 想了一个比较蠢的思路，就是我先递归算出每个节点包含自身和所有子节点的和，然后再递归一次，减去左节点当前的值
# 突然发现想漏了，如果不是根节点的话，最终节点的值应该是其父节点的值加上自己的值，再加上右子树的节点值啊。
class Solution:
    ans = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 突然想到一个，中序遍历搜索数是有序的，从小到大，那么中序遍历倒序是不是从大到小，那不是正好，舒服啊
        if not root:
            return
        if root.right:
            self.convertBST(root.right)
        root.val += self.ans
        self.ans = root.val
        if root.left:
            self.convertBST(root.left)
        return root
