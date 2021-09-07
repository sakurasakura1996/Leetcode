"""
队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1
示例 1：
输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
来源：力扣（LeetCode）
"""
import queue
from collections import deque
class MaxQueue:

    def __init__(self):
        self.deque = deque()   # 双端队列，维护最大值的顺序
        self.queue = queue.Queue()   # 简单队列，单向，维护插入队列值的顺序

    def max_value(self) -> int:
        if self.deque:
            ans = self.deque[0]
            return ans
        else:
            return -1


    def push_back(self, value: int) -> None:
        while  self.deque and value > self.deque[-1]:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)


    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans

