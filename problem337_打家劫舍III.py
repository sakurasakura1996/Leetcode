"""
337. 打家劫舍 III
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
示例 1:
输入: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \
     3   1
输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:
输入: [3,4,5,1,3,null,1]
     3
    / \
   4   5
  / \   \
 1   3   1
输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""
# problem198打家劫舍I， problem213打家劫舍II，题目难度一步一步上升的。
# 主要难度的改变是房屋的排列方式从单链数组->首尾相连的数组->二叉树排列的房屋


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 下面方法提交后超时了，方法应该没错
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         def dfs(root:TreeNode, i:int)->int:
#             if not root:
#                 return 0
#             if i == 0:
#                 return max(dfs(root.left, 0), dfs(root.left, 1)) + max(dfs(root.right, 0), dfs(root.right, 1))
#             if i == 1:
#                 return root.val + dfs(root.left, 0) + dfs(root.right, 0)
#
#         return max(dfs(root, 0), dfs(root, 1))

# 分析别人的题解，大家主要都还是通过递归来写的，但是递归有重复的运算，我上面写的方法还是效率太慢了
# 分析上面的问题，对于一个节点，我都计算了两次，分别为dfs(node,0)和dfs(node,1)，这样不太好
# 记忆化这个东西就是把他们存下来，空间换时间，避免重复的计算，同时一个节点就计算一次，只计算左右节点的子树和
# 找到一个思路相同，但是代码写的比我漂亮的
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root:TreeNode):
            if not root:
                return [0, 0]  # 我上面的偷和不偷在这里表示成数组存储，list[0]表示偷，list[1]表示不偷
            left = dfs(root.left)
            right = dfs(root.right)
            robValue = left[1] + right[1] + root.val
            unrobValue = max(left[0], left[1]) + max(right[0], right[1])
            return [robValue, unrobValue]

        ans = dfs(root)
        return max(ans[0], ans[1])




