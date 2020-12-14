"""
109. 有序链表转换二叉搜索树
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
示例:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 我是不是可以先把链表遍历一遍，然后存在数组中呢
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        if not nums:
            return None
        n = len(nums)

        def toBST(l,r):
            if l >= r:
                return None
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = toBST(l,mid)
            root.right = toBST(mid+1,r)
            return root

        ans = toBST(0, n)
        return ans

