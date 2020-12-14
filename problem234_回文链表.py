"""
234. 回文链表
请判断一个链表是否为回文链表。
示例 1:
输入: 1->2
输出: false
示例 2:
输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 链表问题，我们经常可以使用双指针方法来解决
# 这里的想法就是快慢指针可以先找到链表的中点。但是感觉还不如思路简单点，直接先测试出链表的长度
# 然后再找到中点，开始对比，只不过没能满足O(1)的空间复杂度
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        node = []
        idx = 0

        if cur % 2 == 1:
            while



