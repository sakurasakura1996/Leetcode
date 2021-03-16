class Solution:
    def isValid(self, s: str) -> bool:
        # 用栈来做
        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif ch == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif ch == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif ch == '}':
                if not stack or stack.pop() != '{':
                    return False

        if not stack:
            return True
        else:
            return False

if __name__ == '__main__':
    solu = Solution()
    s = "{[]}"
    ans = solu.isValid(s)
    print(ans)