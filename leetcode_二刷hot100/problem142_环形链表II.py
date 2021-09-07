class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 快慢指针, 数学画图分析下就能得到思路了
        slow, fast = head, head
        flag = 0
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
            if fast == slow:
                flag = 1
                break
        if not flag:
            return None
        ans = head
        while ans != slow:
            slow = slow.next
            ans = ans.next
        return ans


if __name__ == '__main__':
    solu = Solution()
    head = ListNode(3)
    pos = ListNode(2)
    head.next = pos
    pos.next = ListNode(0)
    pos.next.next = ListNode(-4)
    pos.next.next.next = pos
    ans = solu.detectCycle(head)
    print(ans.val)

