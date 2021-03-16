"""
剑指 Offer 06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
"""
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

from typing import List
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        ans = []
        while head:
            ans.insert(0, head.val)
            head = head.next
        return ans

    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]