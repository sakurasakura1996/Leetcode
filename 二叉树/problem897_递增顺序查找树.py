"""
897. 递增顺序查找树
给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。
示例 ：
输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]
       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9
输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
提示：
给定树中的结点数介于 1 和 100 之间。
每个结点都有一个从 0 到 1000 范围内的唯一整数值。
"""
# 简单题的话，暴力法就能解决问题，直接中序遍历完，然后一个一个节点的生成
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        ans = []

        def inorder(root):
            # 中序遍历二叉树，将遍历顺序存入列表
            if not root:
                return None
            if root.left:
                inorder(root.left)
            ans.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        ans_node = TreeNode(None)
        cur_node = ans_node
        for value in ans:
            cur_node.right = TreeNode(value)
            cur_node = cur_node.right
        return ans_node.right

    def increasingBST_2(self, root: TreeNode) -> TreeNode:
        # 那能不能一边遍历的时候就一边把这棵树给构建出来呢,递归和迭代的方法应该都可以，因为遍历到这个节点的时候，我直接将它作为当前叶节点的
        # 右儿子节点
        if not root:
            return None
        ans = TreeNode(None)
        cur = ans

        def inorder(root, cur):
            if not root:
                return None
            if root.left:
                cur = inorder(root.left,cur)
            cur.right = TreeNode(root.val)
            cur = cur.right
            if root.right:
                cur = inorder(root.right,cur)
            return cur
        inorder(root, cur)
        return ans.right
    # 这里用递归方法貌似有点问题，如果指针在调用前更新了好像调用时不能更新了。错了错了，递归也是可以的，只不过你要知道递归的时候如何更新
    # 这个cur指针，返回就可以了啊。

    def increasingBST_3(self, root: TreeNode) -> TreeNode:
        # 上面用了递归方法，那么采用栈结构非递归中序遍历，在遍历过程中构建这棵二叉树当然也是可以的
        # 这就要求熟悉二叉树中序遍历的非递归方法,貌似我又忘了怎么写了，依稀记得要一直向左，直到最左边，然后在出栈，直到第一个有右子节点的，
        # 再继续寻找这个右子节点的最左边子节点
        if not root:
            return None

        stack = []
        ans = TreeNode(None)
        cur = ans
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                root = node.right
                cur.right = TreeNode(node.val)
                cur = cur.right
        return ans.right
        # 方法三是最好的方法。

solu = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)
root.left.left.left = TreeNode(1)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)
ans = solu.increasingBST_2(root)












