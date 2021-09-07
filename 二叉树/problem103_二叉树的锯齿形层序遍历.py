from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        queue = deque()
        if not root:
            return []
        queue.append(root)

        tmp = []
        cur = []
        flag = 0
        while queue:
            node = queue.popleft()
            cur.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            if not queue:
                if flag % 2 == 0:
                    ans.append(cur.copy())
                else:
                    ans.append(cur.copy()[::-1])
                queue.extend(tmp.copy())
                tmp = []
                cur = []
                flag += 1
        return ans

if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    ans = solu.zigzagLevelOrder(root)
    print(ans)
