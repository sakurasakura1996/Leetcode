"""
101.对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
进阶：
你可以运用递归和迭代两种方法解决这个问题吗？
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# way1 递归方法，其间思考时思路有些问题，我们应该把递归的思路想好
class Solution:
    def isDC(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None and B is None:
            return True
        elif A is None and B or A and B is None:
            return False
        else:
            return A.val == B.val and self.isDC(A.left, B.right) and self.isDC(A.right,B.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.isDC(root.left, root.right)

# way2 迭代法 要理解好迭代和递归的区别，递归是该函数要调用自己的，我把它称为套娃哈哈哈
# 而迭代法目前还不太清楚，暂时理解成循环吧。我的最初想法可能可以叫做迭代，因为我的想法是把
# 这棵树准换为一个数组，空的地方用null来代替，就如题目中的例题一样，然后只需要分段来判断该
# 部分中是否是对称的就可以了.实现起来时发现不好搞，最后看题解是根节点入队两次，然后队列中每次取出两个节点
# 这两个节点是必须相等的
from collections import deque
class Solution:
    def isDC(self, A: TreeNode, B: TreeNode) -> bool:
        dq = deque()
        dq.append(A)
        dq.append(B)
        while len(dq) != 0:
            a = dq.popleft()
            b = dq.popleft()
            if a is None and b is None:
                continue
            if ((a is None or b is None) or (a.val != b.val)):
                return False
            dq.append(a.left)
            dq.append(b.right)
            dq.append(a.right)
            dq.append(b.left)
        return True


    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isDC(root, root)






root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
solu = Solution()
ans = solu.isSymmetric(root)
print(ans)

