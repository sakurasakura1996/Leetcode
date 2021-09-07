class Solution:
    def reverseParentheses(self, s: str) -> str:
        # 这种问题感觉肯定要用栈
        stack = []
        for ch in s:
            if ch == '(':
                stack.append('(')
            elif ch == ")":
                string = ""
                while stack and stack[-1] != "(":
                    string = stack.pop() + string
                stack.pop()
                stack.append(string[::-1])
            else:
                stack.append(ch)
        ans = ""
        while stack:
            ans = stack.pop() + ans
        return ans


if __name__ == '__main__':
    solu = Solution()
    s = "a(bcdefghijkl(mno)p)q"
    ans = solu.reverseParentheses(s)
    print(ans)