"""
437. 路径总和 III
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
示例：
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:
1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 题目考察的东西差不多，只不过增加一些要求对题目进行改进限制，主要是路径方向必须向下。
class Solution:
    def pathSum(self, root: TreeNode, summ: int) -> int:
        # 这道题目还是值得关注一下的，搞了大半天没有搞出来的题目，一定要反复体会体会。
        # 下面的代码是错的奥
        ans = 0
        if not root:
            return ans
        if root.val == summ:
            ans += 1
        target = summ - root.val  # 这里这样写就不对了呀，因为题目说并不是一定要从根节点开始才算路径啊，所以这样写不对滴
        left = self.pathSum(root.left, target)
        right = self.pathSum(root.right, target)
        left2 = self.pathSum(root.left, summ)
        right2 = self.pathSum(root.right, summ)
        return ans + left + right + left2 + right2

    def pathSum2(self, root: TreeNode, summ: int) -> int:
        # https://leetcode-cn.com/problems/path-sum-iii/solution/437lu-jing-zong-he-iii-di-gui-fang-shi-by-ming-zhi/
        # 从上面这篇题解中，我发现了我上面递归代码的问题所在，我们很难用一个pathSum函数来理清思路
        # 首先，我们应该理清思路，pathSum函数到底计算的是什么结果。就是题目要求的结果，我们可以不以root为路劲的开始，也可以以root为路径开始
        # 那么问题来了，上面代码中的self.pathSum(root.left, target)又是什么意思，我已经将root作为了路径头节点，然后又可以不选root.left
        # 作为接下来路径上的点吗，这不是有问题了吗，所以一定要想好我们定义的函数的含义。这个题目对自己很有意义
        def countPath(root: TreeNode, target: int) -> int:
            # 这个函数的意思就很确定，从root开始往下走的路径中，路径和为target的路径数目，确定了是以root节点为开始节点
            if not root:
                return 0
            target = target - root.val
            ans = 1 if target == 0 else 0
            return ans + countPath(root.left, target) + countPath(root.right, target)

        if not root:
            return 0
        ans = countPath(root, summ)
        left = self.pathSum2(root.left, summ)
        right = self.pathSum2(root.right, summ)
        return ans + left + right



if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    root.right.right = TreeNode(11)
    ans = solu.pathSum2(root, 8)
    print(ans)
