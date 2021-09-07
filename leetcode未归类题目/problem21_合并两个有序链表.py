"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        cur = ans
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        while l1:
            cur.next = l1
            cur = cur.next
            l1 = l1.next  # 不要忘了这步骤啊，不然while l1不停止循环啊。
        while l2:
            cur.next = l2
            cur = cur.next
            l2 = l2.next
        return ans.next

l1 = ListNode(-9)
l1.next = ListNode(3)


l2 = ListNode(5)
l2.next = ListNode(7)


solu = Solution()
ans = solu.mergeTwoLists(l1,l2)
