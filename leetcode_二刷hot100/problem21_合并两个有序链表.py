class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        ans = ListNode(0)
        p = ans
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return ans.next