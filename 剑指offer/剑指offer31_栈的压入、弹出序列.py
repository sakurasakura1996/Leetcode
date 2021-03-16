"""

"""
from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n = len(pushed)
        push, pop = 0, 0
        while pop < n:
            if stack and stack[-1] == popped[pop]:
                stack.pop()
                pop += 1
            elif push < n and pushed[push] == popped[pop]:
                push += 1
                pop += 1
            elif push < n and pushed[push] != popped[pop]:
                stack.append(pushed[push])
                push += 1
            else:return False
        return True

    # 第二种方法写起来更简单啊，为什么自己写的这么复杂呢。。。。。。直接用一个栈来模拟啊。
    def validateStackSequences2(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)  # num 入栈
            while stack and stack[-1] == popped[i]:  # 循环判断与出栈， 这里的一定得用while循环，写的很精简，
                stack.pop()
                i += 1
        return not stack




if __name__ == '__main__':
    solu = Solution()
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    ans = solu.validateStackSequences(pushed, popped)
    print(ans)
