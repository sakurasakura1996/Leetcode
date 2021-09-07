class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_depth = 0
        y_depth = 0
        x_father = None
        y_father = None
        # 此代码过于丑陋
        def dfs(root, depth):
            if not root:
                return
            nonlocal x_depth, y_depth, x_father, y_father  # 这里一定要写啊，不然不对
            if root.left and root.left.val == x:
                x_depth = depth + 1
                x_father = root
                return
            elif root.left and root.left.val == y:
                y_depth = depth + 1
                y_father = root
                return
            if root.right and root.right.val == x:
                x_depth = depth + 1
                x_father = root
                return
            elif root.right and root.right.val == y:
                y_depth = depth + 1
                y_father = root
                return
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 0)
        if x_father != y_father and x_depth == y_depth:
            return True
        else:
            return False

    def isCousins2(self, root: TreeNode, x: int, y: int) -> bool:
        # x 的信息
        x_parent, x_depth, x_found = None, None, False
        # y 的信息
        y_parent, y_depth, y_found = None, None, False

        def dfs(node: TreeNode, depth: int, parent: TreeNode):
            if not node:
                return

            nonlocal x_parent, y_parent, x_depth, y_depth, x_found, y_found

            if node.val == x:
                x_parent, x_depth, x_found = parent, depth, True
            elif node.val == y:
                y_parent, y_depth, y_found = parent, depth, True

            # 如果两个节点都找到了，就可以提前退出遍历
            # 即使不提前退出，对最坏情况下的时间复杂度也不会有影响
            if x_found and y_found:
                return

            dfs(node.left, depth + 1, node)

            if x_found and y_found:
                return

            dfs(node.right, depth + 1, node)

        dfs(root, 0, None)
        return x_depth == y_depth and x_parent != y_parent




if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    # root.right.right = TreeNode(5)
    ans = solu.isCousins(root, 5, 4)
    print(ans)

