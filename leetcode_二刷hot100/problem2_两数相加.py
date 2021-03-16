class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        flag = 0
        while l1 and l2:
            if l1.val + l2.val + flag < 10:
                num, flag = l1.val + l2.val + flag, 0
            else:
                num, flag = (l1.val + l2.val + flag)%10, 1
            cur.next = ListNode(num)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                if l1.val + flag < 10:
                    num, flag = l1.val + flag, 0
                else:
                    num, flag = (l1.val + flag) %10, 1
                cur.next = ListNode(num)
                cur = cur.next
                l1 = l1.next
        if l2:
            while l2:
                if l2.val + flag < 10:
                    num, flag = l2.val + flag, 0
                else:
                    num, flag = (l2.val + flag) %10, 1
                cur.next = ListNode(num)
                cur = cur.next
                l2 = l2.next
        if flag:
            cur.next = ListNode(flag)
        return head.next


if __name__ == '__main__':
    solu = Solution()
    l1 = ListNode(2)
    l2 = ListNode(5)
    l1.next = ListNode(4)
    ans = solu.addTwoNumbers(l1, l2)
    print(ans.val)
    print(ans.next.val)

