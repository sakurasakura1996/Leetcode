"""
设计并实现最不经常使用（LFU）缓存的数据结构。它应该支持以下操作：get 和 put。
"""
# from collections import OrderdDict
# 有序字典并不能解决问题，还得自己定义数据结构，因为这里需要记录key-value的使用次数，而不止最近使用。
# 
import collections
class Node:
	def __init__(self,key,value,pre=None,next=None,freq=0):
		self.pre = pre
		self.next = next		
		self.value = value
		self.key = key
		self.freq = freq

	def insert(self, next):   # 链表的插入操作
		next.pre = self
		next.next = self.next
		self.next.pre = next
		self.next = next

def create_linked_list():
	head = Node(0, 0)
	tail = Node(0, 0)
	head.next = tail
	tail.pre = head
	return (head, tail)

class LFUCache:
	def __init__(self, capacity: int):
		self.capacity = capacity
		self.size = 0
		self.minFreq = 0
		self.freqMap = collections.defaultdict(create_linked_list)
		self.keyMap = {}

	def delete(self, node):
		if node.pre:
			node.pre.next = node.next
			node.next.pre = node.pre
			if node.pre is self.freqMap[node.freq][0] and node.next is self.freqMap[node.freq][-1]:
				self.freqMap.pop(node.freq)
		return node.key

	def increase(self, node):
		node.freq +=1
		print(node.freq)
		self.delete(node) # 调用一次，频率+1了
		self.freqMap[node.freq][-1].pre.insert(node)
		if node.freq == 1:
			self.minFreq = 1
		elif self.minFreq == node.freq - 1:   # 如果这个新调用的node freq值原来是最小freq值，那么就要看他原来所在的
		# 双链表中除了head tail结点外是否还有节点，如果有就不动，如果没有，那么minfreq也要+1了
			head, tail = self.freqMap[node.freq -1]  # 为什么可以直接这样取到 head 和 tail呢
			if head.next is tail:
				self.minFreq = node.freq

	def get(self, key: int) -> int:
		if key in self.keyMap.keys():
			# 那么就要将它的频率+1，然后移到频率+1为索引的freqMap上去
			self.increase(self.keyMap[key])
			return self.keyMap[key].value
		return -1

	def put(self,key: int, value: int) -> None:
		if self.capacity != 0:
			if key in self.keyMap.keys():
				node = self.keyMap[key]
				node.value = value
			else:
				node = Node(key, value)
				print("++"+str(node.key))
				self.keyMap[key] = node
				print(self.keyMap[key].freq)
				self.size +=1
			if self.size > self.capacity:
				self.size -=1
				deleted = self.delete(self.freqMap[self.minFreq][0].next)
				self.keyMap.pop(deleted)
			print(node.value,node.freq)
			self.increase(node)


    		

        


# Your LFUCache object will be instantiated and called as such:
print("-----")
obj = LFUCache(2)
obj.put(1,1)
a = obj.get(1)
print(a)


