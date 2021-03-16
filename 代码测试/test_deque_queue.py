"""
做了一个题目，发现对python中的数据结构不是很清楚，所以这里尝试看看
"""
import queue

q = queue.Queue()
q.put(2)
q.put(4)
size = q.qsize()    # 队列的长度  等价于 len（）
print(size)
ans = q.get()     # 出队列,并将出队列的元素返回   等价于 pop()
print(ans)
isEmpty = q.empty()
print(isEmpty)

# 上述是 queue包中的 Queue

from collections import deque
# collections库中的 deque是双向队列,可以操作头部和尾部
b = deque()
# deque的操作和python中的列表操作很相似
b.append(2)
b.appendleft(3)
print(b)
len = len(b)
print(len)
print(b.pop())

print("----")
stack = []
stack.append(1)
stack.append(2)
a = stack.pop(1)
print(a)


