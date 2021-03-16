"""
突然想到敲一下这道题
题目意思就是输入一串只包含 左右括号的 字符串，让你输出判断是否是正确的括号匹配
"""
class Solution:
    def isTrue(self, s: str) -> bool:
        # way1,首先用栈来做一编
        stack = []
        for ch in s:
            if ch == '(':
                stack.append('(')
            elif stack:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True

    def isTrue2(self, s: str) -> bool:
        # way2, 使用 O(1)空间复杂度去做，只需要用一个数来记录当前左括号数量就可以啦
        num = 0
        for ch in s:
            if ch == '(':
                num += 1
            elif ch == ')' and num > 0:
                num -= 1
            else:
                return False
        if num > 0:
            return False
        return True


if __name__ == '__main__':
    solu = Solution()
    s = "(())()(("
    ans = solu.isTrue2(s)
    print(ans)