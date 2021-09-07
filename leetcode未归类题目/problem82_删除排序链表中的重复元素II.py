class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 这种题目总是得琢磨很久才能搞对
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        # 那还不如简单点，我们存储下重复出现的数值
        if not head or not head.next:
            return head
        number = set()
        cur = head
        while cur.next:
            if cur.next.val == cur.val:
                number.add(cur.val)
            cur = cur.next
        print(number)
        ans = ListNode(0)
        ans.next = head
        cur = ans
        nxt = head
        while nxt:
            if nxt.val in number:
                nxt = nxt.next
            else:
                cur.next = nxt
                cur = nxt
                nxt = cur.next
        cur.next = nxt
        return ans.next



if __name__ == '__main__':
    solu = Solution()
    head = ListNode(1)
    head.next = ListNode(1)
    # head.next.next = ListNode(1)
    # head.next.next.next = ListNode(2)
    # head.next.next.next.next = ListNode(3)
    ans = solu.deleteDuplicates2(head)
    while ans:
        print(ans.val)
        ans = ans.next

