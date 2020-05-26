"""
206反转链表
进阶：用迭代或递归两种方法来反转链表
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

        class Solution:
            def reverseList(self, head: ListNode) -> ListNode:
                if head is None:
                    return head
                p = head
                node = [head.val]
                while p.next is not None:
                    node.append(p.next.val)
                    p = p.next
                node.reverse()
                # reversed(node)记得上次做过一个题目，这里reversed反转列表，只是暂时的，后面还是没有反转
                p = ListNode(node[0])
                ans = p
                for i in range(1, len(node)):
                    p.next = ListNode(node[i])
                    p = p.next
                return ans


# 上面的写法效率不高。而且进阶也写了要求用迭代和递归分别来写，我这里


