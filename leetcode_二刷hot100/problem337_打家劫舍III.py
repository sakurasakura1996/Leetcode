class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from functools import lru_cache
class Solution:
    # 我想用递归法来试试, 结果是递归可行，下面的代码正确，但是超时了。。。。。但是用记忆化递归勉强通过了。。
    def rob(self, root: TreeNode) -> int:

        @lru_cache(None)
        def my_rob(root, flag):
            if not root:
                return 0
            if flag == 1:
                # flag = 1 表示root节点偷,那么root节点就是可以偷，可以不偷
                left1 = my_rob(root.left, 1)
                left2 = my_rob(root.left, 0)

                right1 = my_rob(root.right, 1)
                right2 = my_rob(root.right, 0)
                return max(left1+right1, left2+right2+root.val)
            else:
                # 表示root上面的节点被偷了，root节点不能偷，那么它的下面的节点是可以偷的
                left = my_rob(root.left, 1)
                right = my_rob(root.right, 1)
                return left + right

        ans = my_rob(root, 1)
        return ans

    def rob2(self, root: TreeNode) -> int:
        # 思路应该就是这样，不过代码层面可以减少点运算复杂度。
        def _rob(root):
            if not root: return 0, 0  # 偷，不偷

            left = _rob(root.left)
            right = _rob(root.right)
            # 偷当前节点, 则左右子树都不能偷
            v1 = root.val + left[1] + right[1]
            # 不偷当前节点, 则取左右子树中最大的值
            v2 = max(left) + max(right)
            return v1, v2

        return max(_rob(root))


if __name__ == '__main__':
    solu = Solution()
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    ans = solu.rob(root)
    print(ans)



