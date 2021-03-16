class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 进阶要求：使用O（1）内存来解决此问题
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodeSet = set()
        if not head:
            return False
        while head:
            if head not in nodeSet:
                nodeSet.add(head)
            else:
                return True
            head = head.next
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        # O（1） 空间复杂度，快慢指针应该可以吧, 这里是简单的判断是否有环，如果让你返回环的开始节点，同样还是快慢指针。但是要推导以下
        fast = slow = ListNode(0)
        fast.next = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
            if fast == slow:
                return True
        return False





if __name__ == '__main__':
    solu = Solution()
    head = ListNode(3)
    second = ListNode(2)
    head.next = second
    second.next = ListNode(0)
    second.next.next = ListNode(-4)
    second.next.next.next = second
    ans = solu.hasCycle(head)
    print(ans)