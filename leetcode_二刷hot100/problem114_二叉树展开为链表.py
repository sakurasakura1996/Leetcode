# 进阶要求，使用原地算法，空间复杂度为O（1）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        # 不考虑空间复杂度，我们可以用个list存起来所有的节点，然后一个一个的连起来就行
        if not root:
            return
        # 还是写下非递归的方法吧
        cur = root
        stack = [root]
        while stack:
            node = stack.pop()
            if node != cur:
                cur.right = node
                cur.left = None
                cur = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def flatten2(self, root: TreeNode):
        # 如果做到原地修改呢，接下来的思路以前考研好像接触到过，这里直接拷贝下来题解的过程
        """
        注意到前序遍历访问各节点的顺序是根节点、左子树、右子树。如果一个节点的左子节点为空，则该节点不需要进行展开操作。
        如果一个节点的左子节点不为空，则该节点的左子树中的最后一个节点被访问之后，该节点的右子节点被访问。该节点的左子树
        中最后一个被访问的节点是左子树中的最右边的节点，也是该节点的前驱节点。因此，问题转化成寻找当前节点的前驱节点。具体做法是，
        对于当前节点，如果其左子节点不为空，则在其左子树中找到最右边的节点，作为前驱节点，将当前节点的右子节点赋给前驱节点的
        右子节点，然后将当前节点的左子节点赋给当前节点的右子节点，并将当前节点的左子节点设为空。对当前节点处理结束后，
        继续处理链表中的下一个节点，直到所有节点都处理结束。
        """
        # 这里的核心一点就是如果一个节点的左节点不为空，那么该节点的左子树中的最后一个节点被访问之后，该节点的右子节点被访问。
        # 所以问题归结到，找到一个节点左子树中最右的节点。
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right



