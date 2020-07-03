""""
这里主要实现的是 二叉树的遍历方法，前序遍历，中序遍历，后序遍历和层次遍历，递归比较好写，这里更加关注非递归的模板编码

"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class DiGuiSolution:
    ans = []
    # 调用遍历函数前记得self.ans.clear()
    def preOrder(self, root:TreeNode) -> List[TreeNode]:
        if not root:
            return None
        self.ans.append(root)
        if root.left:
            self.preOrder(root.left)
        if root.right:
            self.preOrder(root.right)
        return self.ans

    def inOrder(self, root:TreeNode) -> List[TreeNode]:
        if not root:
            return None
        if root.left:
            self.inOrder(root.left)
        self.ans.append(root)
        if root.right:
            self.inOrder(root.right)
        return self.ans

    def postOrder(self, root:TreeNode) -> List[TreeNode]:
        if not root:
            return None
        if root.left:
            self.postOrder(root.left)
        if root.right:
            self.postOrder(root.right)
        self.ans.append(root)
        return self.ans


class FeiDiGuiSolution:
    """"
    采用非递归的方法来进行二叉树的遍历操作，通常都是利用栈或者队列的结构来将递归方法进行转换，递归过程的内部实现，本身就是利用了
    栈的数据结构来进行节点的保存。奥里给！
    """
    def levelOrder(self, root: TreeNode) -> List[TreeNode]:
        # 层次遍历迭代方法实现
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop(0)
            ans.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans

    def inOrder(self, root: TreeNode) -> List[TreeNode]:
        # 中序遍历非递归方法的实现，我们用栈来存储左节点。一直往左遍历。
        if not root:
            return []
        stack = []
        ans = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                root = node.right
                ans.append(node.val)
        return ans

    def preOrder(self, root: TreeNode) -> List[int]:
        # 前序遍历的非递归方法实现，大致可以归结于：非递归方法基本上都需要用到栈。结合前序遍历的顺序，我们可以大致描述非递归方法如下：
        # 根节点入栈后，左节点按顺序一直入栈，此过程中直接将结果全部输出，直到最左端的节点，然后栈顶元素出栈，凡是出栈时该节点的左节点
        # 已经访问过了，直接将其右节点（如果有右节点的话）入栈（入栈时就输出节点值），然后继续找到以该节点为根的子树下最左节点。
        # 简单概括就是入栈时就已经访问了节点，出栈时是为了找其右节点入栈
        if not root:
            return []
        stack = [root]
        ans = [root.val]
        while stack:
            root = stack[-1]
            while root.left:
                ans.append(root.left.val)
                root = root.left
                stack.append(root)
            while not root.right and stack:
                root = stack.pop()
            if root.right:
                ans.append(root.right.val)
                root = root.right
                stack.append(root)
        return ans  # 返回 List[int]和List[TreeNode]都是一样的操作。

    def preOrder_2(self, root: TreeNode) -> List[int]:
        # 先序遍历非递归方法的改进写法，上面是自己的理解，看了别人的思想之后，发现还是写的太乱了
        # 这个优化的方法具体逻辑就是，当前节点，右节点先入栈，左节点后入栈，因为栈的结构是先进后出，符合先序遍历的顺序
        # 然后出栈时，表示访问到该节点，打印其值。这个思想就完完全全是根据先序遍历递归思想而转化来的。
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            cur = stack.pop()
            ans.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return ans




            





solu = FeiDiGuiSolution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

ans = solu.preOrder_2(root)
print(ans)




