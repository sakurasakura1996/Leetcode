"""
用队列实现栈
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here
        """
        self._struc = []

    def push(self, x: int) -> None:
        """
        push element x onto stack
        """
        self._struc.append(x)

    def pop(self) -> int:
        """
        remove the element on top of the stack and returns the element
        """
        return self._struc.pop()

    def top(self) -> int:
        """
        get the top element
        """
        return self._struc[-1]

    def empty(self) -> bool:
        """
        Return whether the stack is empty
        """
        if self._struc:
            return False
        return True

# class MyStack:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.q = []
#
#     def push(self, x: int) -> None:
#         """
#         Push element x onto stack.
#         """
#         self.q.append(x)
#         # q_length = len(self.q)
#         # while q_length > 1:
#         #     self.q.append(self.q.pop(0)) #反转前n-1个元素，栈顶元素始终保留在队首
#         #     q_length -= 1
#
#     def pop(self) -> int:
#         """
#         Removes the element on top of the stack and returns that element.
#         """
#         return self.q.pop()
#
#     def top(self) -> int:
#         """
#         Get the top element.
#         """
#         return self.q[-1]
#
#
#     def empty(self) -> bool:
#         """
#         Returns whether the stack is empty.
#         """
#         return not bool(self.q)


obj = MyStack()

obj.push(3)
obj.push(9)
print(obj.top())
print(obj.pop())
print(obj.top())
# print(obj.empty())


