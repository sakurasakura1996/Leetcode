"""
501. 二叉搜索树中的众数
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
假定 BST 有如下定义：
结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],
   1
    \
     2
    /
   2
返回[2].
提示：如果众数超过1个，不需考虑输出顺序
进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
"""
from typing import List
from collections import Counter
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        return left + [root.val] + right

    def findMode(self, root: TreeNode) -> List[int]:
        counter = Counter(self.inorder(root))
        max_len = max(counter.values())
        return [k for k,v in counter.items() if v == max_len]

# 上述方法并没有实现O(1)的空间复杂度，下面实现了
class Solution:
    def __init__(self):
        self.pre = None
        self.ret = []
        self.ret_count, self.max_count, self.cur_count = 0, 0, 0

    def findMode(self, root: TreeNode) -> List[int]:
        self.inOrder(root)
        self.pre = None
        self.ret = [0] * self.ret_count
        self.ret_count, self.cur_count = 0, 0
        self.inOrder(root)
        return self.ret

    def inOrder(self, root: TreeNode) -> None:
        if not root:
            return
        self.inOrder(root.left)
        if self.pre and self.pre.val == root.val:
            self.cur_count += 1
        else:
            self.cur_count = 1
        if self.cur_count > self.max_count:
            self.max_count = self.cur_count
            self.ret_count = 1
        elif self.cur_count == self.max_count:
            if len(self.ret):
                self.ret[self.ret_count] = root.val
            self.ret_count += 1
        self.pre = root
        self.inOrder(root.right)

# 作者：faterazer
# 链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/solution/zhen-zheng-fu-he-ti-mu-yao-qiu-de-o1kong-jian-fu-z/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
