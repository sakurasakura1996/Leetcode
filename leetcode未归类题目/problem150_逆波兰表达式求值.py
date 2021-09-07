from typing import List
from operator import add, sub, mul
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 逆波兰表达式就是后缀表达式，可以把括号省略，只用数字栈来存储数字即可，遇到数字就入栈，遇到运算符就取出栈顶的两个数字进行运算
        # 然后再将结果压入栈中。
        stack = []
        for token in tokens:
            if token.isdigit():   # 注意奥，'-11'使用isdigit()方法判断不出来是数字哦
                stack.append(int(token))
            elif len(token) > 0 and token[0] == '-':
                stack.append(-int(token[1:]))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    stack.append(num1+num2)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num2 / num1))
        return stack.pop()

    def evalRPN2(self, tokens: List[str]) -> int:
        # 上面的写法说明自己对python的理解还是不够，其实本身有一些通用写法的
        op_to_binary_fn = {
            "+":add,
            "-":sub,
            "*":mul,
            "/": lambda x, y: int(x / y),
        }
        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)
        return stack.pop()


if __name__ == '__main__':
    solu = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    ans = solu.evalRPN(tokens)
    print(ans)