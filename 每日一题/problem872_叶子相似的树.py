class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # 本方法是，中序遍历这两颗二叉树，然后将叶节点序列保存下来，然后对比下
        def getTreeList(root):
            ans = []
            stack = []

            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                if stack:
                    node = stack.pop()
                    if not node.left and not node.right:
                        ans.append(node.val)
                    root = node.right
            return ans
        list1 = getTreeList(root1)
        list2 = getTreeList(root2)
        if len(list1) != len(list2):
            return False
        for num1, num2 in zip(list1, list2):
            if num1 != num2:
                return False
        return True

    def leafSimilar2(self, root1: TreeNode, root2: TreeNode) -> bool:
        # 那能不能用其他方法呢，差不多，深度优先，写一下吧
        def dfs(node: TreeNode):
            if not node.left and not node.right:
                yield node.val
            else:
                if node.left:
                    yield from dfs(node.left)
                if node.right:
                    yield from dfs(node.right)
        seq1 = list(dfs(root1)) if root1 else list()
        seq2 = list(dfs(root2)) if root2 else list()
        return seq1 == seq2



