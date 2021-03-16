class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 进阶要求是 使用O(nlogn)时间复杂度，使用O(1)空间复杂度
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        ans = []
        cur = head
        while cur:
            ans.append(cur.val)
            cur = cur.next
        ans.sort()
        cur = head
        for num in ans:
            cur.val = num
            cur = cur.next
        return head

    def sortList2(self, head: ListNode) -> ListNode:
        # 既然是排序链表，那么我们要想到有什么排序算法是可行的呢，归并排序比较适合
        #　自顶向下归并排序，因为需要递归栈空间，所以其实空间复杂度还不太符合题意
        # 1.找到链表中点，将链表拆分为两个子链表。
        # 2.对两个子链表分别排序
        # 3.将两个排序后的子链表合并，得到完整的排序后的链表。
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            # 左开右闭，尾部是取不到的
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummHead = ListNode(0)
            temp, temp1, temp2 = dummHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummHead.next
        return sortFunc(head, None)

    def sortList3(self, head: ListNode) -> ListNode:
        # 自底向上的归并排序，可以实现O(1)的空间复杂度
        # 意思就是默认开始，子链表长度都是1，然后两两组合，就变成长度为2的链表了，然后再合并，就变成长度为4的链表了，
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            # 上面就是循环的终止条件
            prev, curr = dummyHead, dummyHead.next
            while curr:
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None

                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1

        return dummyHead.next
