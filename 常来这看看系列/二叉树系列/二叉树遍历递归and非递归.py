from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinTree:
    def preOrder(self, root: TreeNode):
        # 二叉树的先序遍历 递归方法
        if not root:
            return
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root: TreeNode):
        # 二叉树的中序遍历， 递归方法
        if not root:
            return
        self.inOrder(root.left)
        print(root.val)
        self.inOrder(root.right)

    def postOrder(self, root: TreeNode):
        # 二叉树的后序遍历 递归方法
        if not root:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val)

    def levelOrder(self, root: TreeNode):
        # 二叉树的层次遍历，即BFS, 二叉树的层次遍历没有递归和非递归的区别了
        # 队列存储节点
        if not root:
            return
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            print(node.val)
            que.append(node.left)
            que.append(node.right)

    def preOrder_nonRecursion(self, root: TreeNode):
        # 二叉树的先序非递归遍历方法,
        # 二叉树先序遍历非递归方法，要多注意注意理解，节点入栈时，我们就要访问节点值或者说输出值，出栈时，我们是为了找到该节点的右节点
        if not root:
            return
        stack = [root]
        print(root.val)
        while stack:
            root = stack[-1]
            while root.left:
                stack.append(root.left)
                print(root.left.val)
                root = root.left
            while not root.right and stack:
                root = stack.pop()
            if root.right:
                print(root.right.val)
                stack.append(root.right)
                root = root.right

    def preOrder_nonRecursion_improved(self, root: TreeNode):
        # 二叉树先序遍历非递归方法的改进版
        if not root:
            return
        stack = [root]
        while stack:
            root = stack.pop()
            print(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

    def inOrder_nonRecursion(self, root: TreeNode):
        # 二叉树的中序非递归遍历方法，一直往左走，使用栈来存取左节点
        if not root:
            return
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                root = node.right
                print(node.val)

    def postOrder_nonRecursion(self, root: TreeNode):
        # 二叉树的后序遍历非递归方法，每个节点都会出现在栈顶两次，只有第二次处于栈顶才能出栈并访问
        # 方法一：用两个栈来实现, 主要记住这个方法吧
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            print(stack2.pop().val)
