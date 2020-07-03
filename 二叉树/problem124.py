"""
124.二叉树中的最大路径和
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
示例 1:
输入: [1,2,3]

       1
      / \
     2   3

输出: 6

示例 2:
输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
"""
# 这题晃着一看，觉得好难，实际它对我来说也确实好难，后来思考了一下，是否可以考虑把这个二叉树考虑成图来做呢
# 一个连通图，然后还没有环，目的就是找到图中最大路径和，找最大路径和又是用的什么方法呢？
# BFS？ DFS？ 拓扑序列？ 最后都想不出来，我哭了。。。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = float("-inf")

    def maxGain(self, root: TreeNode) -> int:

        if not root:
            return 0
        leftsum = self.maxGain(root.left)
        rightsum = self.maxGain(root.right)
        cur_sum = root.val + leftsum + rightsum
        self.ans = max(self.ans, cur_sum)
        return max(root.val, root.val+max(leftsum, rightsum))

    def maxPathSum(self, root: TreeNode) -> int:
        cur_ans = self.maxGain(root)
        return max(cur_ans, self.ans)



solu = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

ans = solu.maxPathSum(root)
print(ans)

"""
看了题解之后，记录一下思路点吧：
先不讨论题解哪里用到了DFS，直接分析题意。
这道题主要解题点在于以节点 i 为根的路径和是怎么来的，假设以节点 i 为根的路径（注意路径的概念，只能是 i 的左边加 i 或者 i 的右边加 i ）
向其父节点能贡献的值可以由函数 f(i) 得到，可以得到 i 为根的路径和最大值为：
root.val + Math.max(f(root.left), 0) + Math.max(f(root.right), 0)
毕竟由 i 的左右节点贡献的值有可能是负数，所以要排除负数的影响。
再来讨论 f(i) 本身，这个函数的返回值应该是：
f(i) = Math.max(Math.max(f(i.left), f(i.right)), 0) + i.val;
同样的，先排除i的左右子节点贡献负值的可能性，然后选其中的较大值，加上本节点的值就是本节点能向其父节点贡献的值。
上面这两段话其实就是官方题解的最核心部分，以后看到类似这种路径和最大、路径和为某值的题往这种思路上套就奥利给了。

这种题的思路就是两条线：一条线是以该节点为根节点来构造一个路径和，将它作为最终路径来计算路径和，也就是根节点加上左右节点的贡献
还有一条线就是该节点并不是最高层的节点，而是要贡献给该节点的父节点去，那么这个时候，就不能都选择该节点的左右子节点了。
"""
