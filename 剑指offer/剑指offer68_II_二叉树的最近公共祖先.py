class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 用java在写这道题，感觉dfs写的好晕，用python 理清思路。
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = []
        path_q = []
        flag = True

        def backtrace(root, target, cur):
            nonlocal flag
            # 找到从root到target的路径，然后返回路径上所有节点
            if root == target:
                cur.append(root)
                flag = False
                return cur
            if not root:
                return
            cur.append(root)
            backtrace(root.left, target, cur)
            backtrace(root.right, target, cur)
            # 这里不能无条件的 出栈啊。 设置一个flag，如果没有找到target就pop啊
            if flag:
                cur.pop()

        backtrace(root, p, path_p)
        flag = True
        backtrace(root, q, path_q)

        for node in path_p:
            print(node.val)
        print("--")
        for node in path_q:
            print(node.val)
        i = 0

        while i < len(path_p) and i < len(path_q):
            if path_p[i] == path_q[i]:
                ans = path_p[i]
            else:
                break
            i += 1
        return ans

if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(3)
    root.left =TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    ans = solu.lowestCommonAncestor(root, root.left, root.left.right.right)
    print(ans.val)

