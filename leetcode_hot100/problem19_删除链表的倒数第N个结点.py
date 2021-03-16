"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？
示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]
提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return None
        pre, cur = None, head
        for i in range(n):
            cur = cur.next
        while cur:
            cur = cur.next
            if not pre:
                pre = head
            else:
                pre = pre.next
        if not pre:
            return head.next
        else:
            pre.next = pre.next.next
            return head

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # 上面的代码写的还是太丑了啊，下面写的这么简洁呢，好好学习学习
        dummy = ListNode(0, head)   # 链表这一步很重要，如果最后实际删除的是头节点
        # 这个时候代码就不好写了，那我们可以在头节点前面在写一个节点啊，不就很好搞了嘛
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


if __name__ == '__main__':
    solu = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    ans = solu.removeNthFromEnd(head, 2)
    while ans:
        print(ans.val)
        ans = ans.next


