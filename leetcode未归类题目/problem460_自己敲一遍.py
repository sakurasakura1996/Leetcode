import collections

class Node:
	def __init__(self,key,value,pre=None,next=None,freq=0):
		self.pre = pre
		self.next = next
		self.key = key
		self.value = value
		self.freq = freq

	def insert(self, node):
		node.pre = self
		node.next = self.next
		self.next.pre = node
		self.next = node

def create_linked_list():
	head = Node(0,0)
	tail = Node(0,0)
	head.next = tail
	tail.pre = head
	return (head,tail)

class LFUCache:
	def __init__(self,capacity:int):
		self.capacity = capacity
		self.size = 0
		self.minFreq = 0
		self.freqMap = collections.defaultdict(create_linked_list)
		self.keyMap = {}

	def delete(self, node):
		# 删除节点
		if node.pre:
			node.pre.next = node.next
			node.next.pre = node.pre
			if node.pre is self.freqMap[node.freq][0] and node.next is self.freqMap[node.freq][-1]:
				self.freqMap.pop(node.freq)
		return node.key

	def increase(self, node):
		# 该节点的freq+1，然后更换一下他在freqMap的位置
		node.freq +=1
		self.delete(node)
		self.freqMap[node.freq][-1].pre.insert(node)
		if node.freq == 1:
			self.minFreq = 1
		elif self.minFreq == node.freq-1:
			head, tail = self.freqMap[node.freq-1]
			if head.next is tail:
				self.minFreq = node.freq

	def get(self, key:int) -> int:
		if key in self.keyMap.keys():
			self.increase(self.keyMap[key])
			return self.keyMap[key].value
		return -1

	def put(self,key: int,value: int) -> None:
		if self.capacity!=0:
			if key in self.keyMap.keys():
				node = self.keyMap[key]
				node.value = value
			else:
				node = Node(key, value)
				self.keyMap[key] = node
				self.size +=1
			if self.size > self.capacity:
				self.size -=1
				deleted = self.delete(self.freqMap[minFreq][0].next)
				self.keyMap.pop(deleted)
			self.increase(node)

obj = LFUCache(2)
obj.put(1, 1)
a = obj.get(1)
print(a)