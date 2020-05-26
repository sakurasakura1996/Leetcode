"""
最长有效括号   给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
可惜这道题我还是没有自己独立想出来用动态规划来解决，还是后面看题解的
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        else:
            maxlen = 0
            length = len(s)
            ans = [0]*length
            for i in range(1, length):
                if s[i] == ')':
                    # 那么就往前找左括号去匹配
                    if s[i-1] == '(':
                        # ans[i] = ans[i-2]+2   卧槽，这里一定要注意，这里i=1时，不会出现数组越界的情况，
                        # 因为s[-1]指向最后一个字符，所以一定要小心
                        if i>=2:
                            ans[i]=ans[i-2]+2
                        else:
                            ans[i]=2
                    else:
                        if (i-ans[i-1]) >0 and s[i-ans[i-1]-1] == '(':
                            if i-ans[i-1]-1 >= 2:
                                ans[i] = ans[i-ans[i-1]-2]+ans[i-1]+2
                            else:
                                ans[i] = ans[i-1]+2
        return max(ans)


s = "(()))"
solu = Solution()
answer = solu.longestValidParentheses(s)
print(answer)


