"""
剑指 Offer 25. 合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
示例1：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：
0 <= 链表长度 <= 1000
注意：本题与主站 21 题相同
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:return l2
        if not l2:return l1
        ret = ListNode(0)
        ans = ret
        while l1 and l2:
            if l1.val <= l2.val:
                ans.next = l1
                l1 = l1.next
                ans = ans.next
            else:
                ans.next = l2
                l2 = l2.next
                ans = ans.next
        if l1:
            ans.next = l1
        else:
            ans.next = l2
        return ret.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    solu = Solution()
    ans = solu.mergeTwoLists(l1, l2)
    while ans:
        print(ans.val)
        ans = ans.next

