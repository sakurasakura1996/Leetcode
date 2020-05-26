"""
876 链表的中间节点
给定一个带有头节点head的非空单链表，返回链表的中间节点
如果有两个中间节点，则返回第二个中间节点
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 注意这里的head头节点已经存了第一个值，我理解错了
        length = 1
        ans = head
        while ans.next != None:
            length+=1
            ans = ans.next
        # 求出链表的长度之后，再找到位于中间位置的
        # print(length)
        length = int(length/2)+1
        ans = head
        while length>1:
            ans = ans.next
            length -=1
        return ans
