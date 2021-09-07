from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        # 我们可以采用层次遍历的方法来做。
        if not root:
            return root
        queue = deque()
        queue.append(root)
        tmp = []
        pre = None
        while queue:
            node = queue.popleft()
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            if pre:
                pre.next = node
                pre = node
            if not pre:
                pre = node
            if not queue:
                queue.extend(tmp.copy())
                tmp = []
                pre = None
        return root

if __name__ == '__main__':
    solu = Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    ans = solu.connect(root)
    print(ans.val)
    print(ans.left.next.val)
    print(ans.right.val)

