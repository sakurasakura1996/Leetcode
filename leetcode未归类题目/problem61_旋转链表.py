class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 实例给的好，不然我们可能会很容易忘记如果k大于链表的长度怎么办啊,这道题相当于在k值取余链表长度之后得到 m，然后取出倒数第m个链表节点
        if k == 0 or not head or not head.next:
            return head

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        k = k % length


        cur = p = head
        for i in range(k):
            p = p.next
        while p.next:
            p = p.next
            cur = cur.next
        ans = cur.next
        p.next = head
        cur.next = None
        return ans

if __name__ == '__main__':
    solu = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    ans = solu.rotateRight(head, 2)
    while ans:
        print(ans.val)
        ans = ans.next


