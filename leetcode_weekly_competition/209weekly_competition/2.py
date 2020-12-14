# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from collections import defaultdict
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        # 第一直觉：使用层次遍历。
        heap = deque()
        heap.append(root)
        level = 0
        level_list = []
        if root.val % 2 == 0:
            return False
        while heap:
            node = heap.popleft()
            if level % 2 == 0:
                if node.left and node.left.val % 2 != 0:
                    return False
                if node.left and not level_list:
                    level_list.append(node.left)
                elif node.left and level_list:
                    if node.left.val >= level_list[-1].val:
                        return False
                    else:
                        level_list.append(node.left)
                if node.right and node.right.val % 2 != 0:
                    return False
                if node.right and not level_list:
                    level_list.append(node.right)
                elif node.right and level_list:
                    if node.right.val >= level_list[-1].val:
                        return False
                    else:
                        level_list.append(node.right)
            else:
                if node.left and node.left.val % 2 == 0:
                    return False
                if node.left and not level_list:
                    level_list.append(node.left)
                elif node.left and level_list:
                    if node.left.val <= level_list[-1].val:
                        return False
                    else:
                        level_list.append(node.left)

                if node.right and node.right.val % 2 == 0:
                    return False
                if node.right and not level_list:
                    level_list.append(node.right)
                elif node.right and level_list:
                    if node.right.val <= level_list[-1].val:
                        return False
                    else:
                        level_list.append(node.right)
            if not heap:
                heap.extend(level_list.copy())
                level_list.clear()
                level += 1
        return True
    # 上面的方法确实通过了，但是写的代码也太狗屎了吧
    # 下面的写法是大佬们的方法，可以学一学。
    def isEvenOddTree2(self, root: TreeNode) -> bool:
        infor = defaultdict(lambda: [])

        def visit(node=root, l=0):
            if node is None:
                return
            visit(node.left, l + 1)
            infor[l].append(node.val)
            visit(node.right, l + 1)

        visit()
        # 这位大佬的思路就是，我先把所有的结果存起来，然后再来判断。
        for k in infor:
            for t in infor[k]:
                if not (k + t) % 2 == 1:
                    return False

            for i in range(len(infor[k]) - 1):
                if k % 2 == 1 and infor[k][i] <= infor[k][i + 1]:
                    return False
                if k % 2 == 0 and infor[k][i] >= infor[k][i + 1]:
                    return False
        return True







