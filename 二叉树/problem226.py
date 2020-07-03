"""
226.翻转二叉树
"""
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root or (root.left == None and root.right == None):
            return root
        tmp_left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp_left)
        return root

# 二叉树类的题目多半可以用递归来解决，这还是蛮好的哈哈哈，但是就怕你不会非递归方法啊
    def invertTree_2(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        # 题解中还有使用了迭代的方法来解决。这种做法和BFS很接近
        # 这个方法的思路就是我们需要交换所有节点的左孩子和右孩子。因此可以创建队列来
        # 存储所有左孩子右孩子还没有交换过的节点。开始的时候，只有根节点在队列中，只要队列
        # 不为空，则一直出队列，然后互换这个节点的左右孩子节点，接着再把孩子节点入队到队列，
        # 对于其中的空节点则不需要加入队列
        # 同时注意，原则上只要能够遍历二叉树的方法都可以解决这个问题。
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            tmp = node.right
            node.right = node.left
            node.left = tmp
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return root

    # 那我们再试试其他的遍历方法可不可行，上面的解法是层次遍历，这里使用中序看看行不行
    def invertTree_3(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        # 上面判断子节点是否为空是多余操作
        stack = []
        ans = root
        while stack or root:
            while root:
                stack.append(root)
                tmp = root.right
                root.right = root.left
                root.left = tmp
                # stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                root = node.right
        return ans

    def invertTree_4(self, root: TreeNode) -> TreeNode:
        # 这里再试试前序行不行，需要了解前序遍历的非递归方法，具体可以参考code_template
        # 先序遍历非递归方法在进栈时，先让右节点进栈，那么现在翻转二叉树的
        if not root:
            return root
        stack = [root]
        ans = root
        while stack:
            node = stack.pop()
            tmp = node.right
            node.right = node.left
            node.left = tmp
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans





solu = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

ans = solu.invertTree_4(root)
print(ans.left.right.val)

