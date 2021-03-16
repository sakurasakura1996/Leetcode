class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 进阶要求O（n)时间复杂度 和 O(1)的空间复杂度来解决此题
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        left, right = 0, len(ans)-1
        while left < right:
            if ans[left] != ans[right]:
                return False
            left += 1
            right -= 1
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        # O（n）时间复杂度， O（1）空间复杂度， 快慢指针方法，不知道为啥，总是搞不出来这种高效的解法
        # 我们可以将链表的后半部分反转（修改链表结构）然后将前半部分和后半部分进行比较。



