class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = ListNode(0)
        prev.next = head
        ans = prev
        while head and head.next:
            cur = head.next
            head.next = cur.next
            cur.next = head
            prev.next = cur
            prev = head
            head = head.next
        return ans.next


if __name__ == '__main__':
    solu = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    ans = solu.swapPairs(head)
    while ans:
        print(ans.val)
        ans = ans.next
