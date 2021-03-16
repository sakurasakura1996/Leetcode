from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        level = []
        tmp = []
        while queue:
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            if not queue:
                ans.append(level.copy())
                queue.extend(tmp.copy())
                tmp = []
                level = []
        return ans

if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    ans = solu.levelOrder(root)
    print(ans)



