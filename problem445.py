"""
两数相加II：给你两个非空链表来代表两个非负整数，数字最高位位于链表开始位置。它们的每个节点
只存储一位数字。将这两数相加会返回一个新的链表。 可以假设除了数字0之外，这两个数字都不会以0开头。
两个数字相加会返回一个新的链表。
进阶：如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
"""
from typing import List
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def calList(self, l1:ListNode)->int:
		ans = l1.val
		while l1.next!=None:
			ans = ans * 10 + l1.next.val
			l1 = l1.next
		return ans
	def addTwoNumbers(self, l1:ListNode, l2:ListNode)-> ListNode:
		ans = self.calList(l1) + self.calList(l2)
		NodeList = [i for i in str(ans)]
		# print(NodeList)
		ans = ListNode(int(NodeList[0]))
		p = ans
		for i in range(1,len(NodeList)):
			ans.next = ListNode(int(NodeList[i]))
			ans = ans.next
		return p




solu = Solution()
l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
ans = solu.addTwoNumbers(l1,l2)
print(ans.val)
while ans.next!=None:
	print(ans.next.val)
	ans = ans.next