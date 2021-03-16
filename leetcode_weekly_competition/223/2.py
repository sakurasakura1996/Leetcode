class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # 实在不行，用最蠢的办法算了
        ans = head
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        head = ans
        n = len(arr)
        for i in range(n):
            if i == k-1:
                head.val = arr[n-k]
            if i == n - k:
                head.val = arr[k-1]
            head = head.next
        return ans




