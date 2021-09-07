class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        # 总是想的比较复杂，我们争取简单点思考
        less_node = ListNode(0)
        cur = less_node
        more_node = ListNode(0)
        cur2 = more_node
        while head:
            if head.val < x:
                cur.next = head
                cur = cur.next
                head = head.next
                cur.next = None
            else:
                cur2.next = head
                cur2 = cur2.next
                head = head.next
                cur2.next = None

        cur.next = more_node.next
        return less_node.next


if __name__ == '__main__':
    solu = Solution()
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    ans = solu.partition(head, 3)
    while ans:
        print(ans.val)
        ans = ans.next



