"""
题目描述
输入一个链表，反转链表后，输出新链表的表头。
示例1
输入
复制
{1,2,3}
返回值
复制
{3,2,1}
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead: ListNode):
        if not pHead or not pHead.next:
            return pHead
        cur = pHead
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    solu = Solution()
    b = solu.ReverseList(a)
    print(b.val)
    print(b.next.val)
    print(b.next.next.val)