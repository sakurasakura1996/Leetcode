"""
143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例 1:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        # 一定要考虑特殊情况
        if not head:
            return
        fast = head
        slow = head
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next
            else:
                break
        # 此时的slow指向的就是最后链表的终点了。
        point = []
        end = slow
        while slow.next:
            slow = slow.next
            point.append(slow)
        start = head
        while point:
            insert = point.pop()
            insert.next = start.next
            start.next = insert
            start = insert.next
        end.next = None

    def reorderList2(self, head: ListNode) -> None:
        if not head:
            return
        vec = list()
        node = head
        while node:
            vec.append(node)
            node = node.next

        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        vec[i].next = None



