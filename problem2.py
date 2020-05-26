"""
链表两数相加，返回结果的链表表示
"""
class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		if l1.val == 0 and l1.next==None:
			return l2
		if l2.val == 0 and l2.next==None:
			return l1
		ans = ListNode(l1.val+l2.val)
		p = ans
		flag = 0
		while l1 != None and l2!= None:   # 后面发现这种表达完全无效，程序根本没有从这里进入
			ans.next = ListNode(l1.val+l2.val)
			l1 = l1.next
			l2 = l2.next
			ans = ans.next
		if l1==None:
			print("l1=None")
			while l2!=None:
				ans.next = ListNode(l2.val)
				l2 = l2.next
				ans = ans.next
		if l2 == None:
			print("l2=None")
			while l1!=None:
				ans.next = ListNode(l1.val)
				l1 = l1.next
				ans = ans.next

		ans = p.next
		print("hello")
		print(ans.val)
		while ans.next!=None:
			print(ans.next.val)
			ans =ans.next
		ans = p.next
		while ans.next!=None:
			if ans.val+flag > 9:
				ans.val = ans.val+flag -10
				flag = 1
			else:
				ans.val = ans.val+flag
				flag = 0
			ans = ans.next
		if ans.val + flag > 9:
			ans.val = ans.val+flag-10
			ans.next = ListNode(1)
		else:
			ans.val = ans.val+flag
		ans = p.next
		p.next = None
		return ans

l1 = ListNode(0)
l1.next = ListNode(8)
l1.next.next = ListNode(6)

l2 = ListNode(6)
l2.next = ListNode(7)
l2.next.next = ListNode(8)

solu = Solution()
ans = solu.addTwoNumbers(l1,l2)

print(ans.val)
print(ans.next.val)




