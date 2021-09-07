class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 题目的进阶要求是使用 迭代 和 递归 方法来分别求解。
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

if __name__ == '__main__':
    solu = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    ans = solu.reverseList(head)
    while ans:
        print(ans.val)
        ans = ans.next




