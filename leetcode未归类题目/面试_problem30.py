"""
包含min函数的栈
"""
class MinStack:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stack = []

	def push(self, x:int) -> None:
		self.stack.append(x)

	def pop(self)->None:
		if len(self.stack)>0:
			self.stack = self.stack[:-1]

	def top(self)->int:
		return self.stack[-1]

	def min(self)->int:
		return min(self.stack)

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.min())
obj.pop()
print(obj.top())
print(obj.min())
