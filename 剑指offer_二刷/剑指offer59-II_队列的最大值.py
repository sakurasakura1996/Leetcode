"""
剑指 Offer 59 - II. 队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1
示例 1：
输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

示例 2：
输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
限制：
1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
"""
from collections import deque
class MaxQueue:

    def __init__(self):
        self.que = deque()
        self.maxque = deque()
        self.maxvalue = 0


    def max_value(self) -> int:
        if not self.que:
            return -1
        return self.maxque[0]

    def push_back(self, value: int) -> None:
        self.que.append(value)
        if value > self.maxvalue:
            self.maxvalue = value
            self.maxque.append(value)
        else:




    def pop_front(self) -> int:
