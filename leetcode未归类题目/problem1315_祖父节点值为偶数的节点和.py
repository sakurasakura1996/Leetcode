"""
1315. 祖父节点值为偶数的节点和
给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：
该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
如果不存在祖父节点值为偶数的节点，那么返回 0 。
示例：
输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：18
解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。
提示：
树中节点的数目在 1 到 10^4 之间。
每个节点的值在 1 到 100 之间。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def search(root, flag):
            # flag = 0, 1, 2, 0表示当前节点是爷爷，1表示是爸爸，0表示是儿子
            # 函数定义为root.val为偶数，找到该节点的孙子总和
            if not root:
                return 0
            if flag == 2:
                return root.val
            if flag == 1:
                return search(root.left, 2) + search(root.right, 2)
            if flag == 0:
                return search(root.left, 1) + search(root.right, 1)

        if not root:
            return 0
        ans = 0
        if root.val % 2 == 0:
            ans += search(root, 0)
        return ans + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)


if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(6)
    root.left = TreeNode(7)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)
    ans = solu.sumEvenGrandparent(root)
    print(ans)



