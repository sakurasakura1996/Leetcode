"""
234. 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 无脑的方法就是遍历一遍链表，将所有元素值存入list中判断是否回文
        cur = []
        while head:
            cur.append(head.val)
            head = head.next
        if not cur:
            return True
        n = len(cur)
        for i in range(n//2):
            if cur[i] != cur[n-i-1]:
                return False
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        # 要求用O(1)的空间复杂度来做。
        # 一定要注意写特殊情况
        if not head or not head.next:
            return True
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            # 如果链表有奇数个节点，那么slow指向中间节点，如果链表有偶数个节点，slow指向左半部分结尾节点

        right = self.reverse_list(slow.next)
        left = head
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverse_list(self, head: ListNode):
        # 从head节点开始翻转链表
        pre = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         # 下面的解法不知道什么时候写的了，空间复杂度还是偏高，这道题如果用O（1）空间复杂度的话，还是需要重视理解一下的。
#         fast = head
#         slow = head
#         if not head or not head.next:
#             return True
#         if not head.next.next:
#             return head.val == head.next.val
#         length = 1
#         node = []
#         while fast.next:
#             fast = fast.next
#             length += 1
#             node.append(slow.val)
#             if fast.next:
#                 fast = fast.next
#                 length += 1
#                 slow = slow.next
#
#         if length % 2 == 1:
#             # slow 指向中间节点，
#             cur = slow.next
#             while node and cur:
#                 if node[-1] != cur.val:
#                     return False
#                 node.pop()
#                 cur = cur.next
#         else:
#             # slow 指向左半部分最后的节点
#             cur = slow.next
#             node = node[:-1]
#             while node and cur:
#                 if node[-1] != cur.val:
#                     return False
#                 node.pop()
#                 cur = cur.next
#         return True


if __name__ == '__main__':
    solu = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(1)
    ans = solu.isPalindrome2(head)
    print(ans)