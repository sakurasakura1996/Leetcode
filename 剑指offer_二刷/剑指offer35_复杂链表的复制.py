"""
copyRandomList函数，复制一个复杂链表出来
"""
from collections import defaultdict
class Node:
    def __init__(self, x: int, next: 'Node'=None, random: 'Node'=None):
        self.val = x
        self.next = next
        self.random = random

# 想法是通过哈希表来存储原来链表各节点
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:return head
        list_dict = {}
        cur = head
        while cur:
            list_dict[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            list_dict[cur].next = list_dict.get(cur.next)
            list_dict[cur].random = list_dict.get(cur.random)
            cur = cur.next
        return list_dict[head]

