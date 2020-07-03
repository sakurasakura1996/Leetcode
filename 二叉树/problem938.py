"""
938.二叉搜索树的范围和
给定二叉搜索树的根节点root，返回L和R（含）之间的所有节点的值的和
二叉搜索树保证具有唯一指定的值
实例：
输入：root = root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32
提示：
树中的结点数量最多为 10000 个。
最终的答案保证小于 2^31。
"""
# 二叉搜索树是有序的，如果想要从小到大的读出数字，那么采用中序遍历就行了，然后只需要在取到值的时候
# 判断下是否在 L，R之间，如果在就加入到存储变量ans中就ok了
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
#         ans = 0
#         if not root:
#             return ans
#         left_ans = self.rangeSumBST(root.left, L, R)  # 可以根据mid_ans来省去一部分的递归程序用时。
#         mid_ans = root.val
#         right_ans = self.rangeSumBST(root.right, L, R)
#         if L <= mid_ans <= R:
#             ans += (mid_ans + left_ans + right_ans)
#         else:
#             ans += (left_ans + right_ans)
#         return ans

# way2 还可以用DFS来做，DFS又可以用递归方法和迭代方法来写
# 递归方法，思路比较简单
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if R > node.val:
                    dfs(node.right)
        self.ans = 0
        self.dfs(root)
        return self.ans

# 感觉上面这种写法不是太喜欢。我自己写写看
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        ans = 0
        if L <= root.val <= R:
            ans += root.val
        if L < root.val:
            ans += self.rangeSumBST(root.left, L, R)
        if R > root.val:
            ans += self.rangeSumBST(root.right, L, R)
        return ans


# 迭代实现DFS
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int)->int:
        if not root:
            return 0
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if R > node.val:
                    stack.append(node.right)
        return ans


solu = Solution()
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
ans = solu.rangeSumBST(root, 7, 15)
print(ans)