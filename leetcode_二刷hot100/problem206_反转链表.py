class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 要求使用递归方法 或 迭代方法 来反转链表，要求使用两种方法解决这道题
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归方法, 真的是不是二叉树的问题，用递归想起来就没那么简单啊
        # 感觉递归方法写的不是太好啊
        if not head:
            return head

        def recur(head: ListNode, pre: ListNode):
            if head:
                tmp = head.next
                head.next = pre
                pre = head
                ans = recur(tmp, pre)
                return ans
            else:
                return pre
        ans = recur(head, None)
        return ans

    def reverseList2(self, head: ListNode) -> ListNode:
        # 迭代法
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reverseList3(self, head: ListNode) -> ListNode:
        # 这种写法还是挺想的好
        if not head or not head.next:
            return head
        p = self.reverseList3(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == '__main__':
    solu = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    ans = solu.reverseList3(head)
    while ans:
        print(ans.val)
        ans = ans.next
