"""
147. 对链表进行插入排序
对链表进行插入排序。
插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
插入排序算法：
插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
示例 1：
输入: 4->2->1->3
输出: 1->2->3->4

示例 2：
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 每次感觉自己如何描述插入排序或者说如何用程序语言描述内心所想的过程，总是没有那么顺畅的感觉啊。
        cur = head
        while cur.next:
            p = cur.next
            if p.val >= cur.val:
                cur = cur.next
            else:
                if p.val < head.val:
                    cur.next = p.next
                    p.next = head
                    head = p
                else:
                    tmp = head
                    while p.val > tmp.next.val:
                        tmp = tmp.next
                    cur.next = p.next
                    p.next = tmp.next
                    tmp.next = p
        return head

    # 上面的代码是自己写的，总觉得自己的思考过程很别扭，不是很舒服
    # 我们再学习学习下面这个代码的逻辑性，是不是让人看起来舒服太多了啊，好好学学吧
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        # 不是说了吗，一般这种问题可以先创建一个哑节点
        first = ListNode(0, head)
        # 然后我们想好到底需 要指示哪几个指针啊
        lastSorted = head  # 已经排好序的节点
        cur = head.next   # 接下来准备排序的节点
        while cur:
            if lastSorted.val <= cur.val:
                lastSorted = lastSorted.next
            else:
                prev = first
                while prev.next.val <= cur.val:
                    prev = prev.next
                lastSorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = lastSorted.next
        return first.next




if __name__ == '__main__':
    solu = Solution()
    head = ListNode(4)
    head.next = ListNode(3)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(5)
    ans = solu.insertionSortList(head)
    while ans:
        print(ans.val)
        ans = ans.next








