"""
题目描述：编写一个简单计算器，只考虑四个运算符 + - * / 且参与运算的数值都为非负整数
多组样例，每个测试样例占一行，每行不超过200个字符， 整数与运算符之间有一个空格，没有非法表达式，当一行输入0时，输入结束
"""
from collections import deque
s = input()
input_ = s.split(" ")
number_stack = deque()
stack = deque()
start = 0
while start < len(input_):
    if input_[start] == '+':
        stack.append('+')
        start += 1
    elif input_[start] == '-':
        stack.append('-')
        start += 1
    elif input_[start] == '*':
        # 取出栈顶的数和接下来的数
        top = number_stack.pop()
        latter = int(input_[start+1])
        number_stack.append(top * latter)
        start += 2
    elif input_[start] == '/':
        top = number_stack.pop()
        latter = int(input_[start+1])
        number_stack.append(top / latter)
        start += 2
    else:
        number_stack.append(int(input_[start]))
        start += 1
while stack:
    op = stack.popleft()
    if op == '+':
        number_stack.appendleft(number_stack.popleft() + number_stack.popleft())
    elif op == '-':
        number_stack.appendleft(number_stack.popleft() - number_stack.popleft())
print(round(number_stack.pop(), 2))