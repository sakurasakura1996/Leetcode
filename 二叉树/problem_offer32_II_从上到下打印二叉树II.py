"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行
本题与主站102题相同
"""
from typing import List
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 相当于层次遍历嘛，但是问题在于我要确保每一层节点值保存在一个列表中,那么我可以 用一个指针来指示每层最右边的节点。或者我每一层的节点先用
        # 一个列表存起来，当栈中最后一个节点出栈了，这时候，我将例表中的节点加入到栈中即可
        ans = []
        if not root:
            return []
        stack = [root]
        next_level = []
        next_level_value = []
        ans.append([root.val])
        while stack:
            node = stack.pop(0)
            if node.left:
                next_level.append(node.left)
                next_level_value.append(node.left.val)
            if node.right:
                next_level.append(node.right)
                next_level_value.append(node.right.val)

            if not stack and next_level:
                # 若此时栈为空了，则把列表中存储的下一层的节点压入栈中,同时，这列表中存储的也就是答案需要的那个列表啊
                stack.extend(next_level)
                # ans.append(next_level_value)  后面next_level_value会清空，这样写，一旦后面清空，这里共享内存的内容也会清空了
                value = next_level_value.copy()  # 避免直接加入共享内存会删除结果
                ans.append(value)
                next_level.clear()
                next_level_value.clear()  # 卧槽，发现代码问题在这，在前两行，我把列表值加入到ans中后，这里要清空，
                # 结果这里清空后ans中也对应空了，这特么是共享内存了吗？改为用copy()
        return ans


solu = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left =TreeNode(15)
root.right.right = TreeNode(7)
ans = solu.levelOrder(root)
print(ans)