"""

"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # 先用递归的方法试试
        if not root:
            return []
        val = root.val
        if val == sum and not root.left and not root.right:
            return [[val]]
        ans = []
        if root.left:
            for value in self.pathSum(root.left, sum - val):
                ans.append([val]+value)
        if root.right:
            for value in self.pathSum(root.right, sum - val):
                ans.append([val] + value)
        return ans

    def pathSum2(self, root: TreeNode, summ: int) -> List[List[int]]:
        # 用其他方法做做看 DFS, 回溯等方法
        if not root:
            return []
        ans = []

        def backtrace(root: TreeNode, path: List[int], summ:int):
            s = sum(path)
            if not root.left and not root.right:
                if s == summ:
                    ans.append(path.copy())  # 这里一定要加copy()啊
                    return
                else:
                    return
            # print(type(root))
            if root.left:
                path.append(root.left.val)
                backtrace(root.left, path, summ)
                path.pop()
            if root.right:
                path.append(root.right.val)
                backtrace(root.right, path, summ)
                path.pop()
        backtrace(root, [root.val], summ)
        return ans

    # 下面这种别人写的代码还是简洁清晰啊。。。
    def pathSum3(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []

        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res


if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    summ = 9
    ans = solu.pathSum2(root, summ)
    print(ans)
