"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        n = len(s)
        if n%2 == 1:
            return False

        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = list()
        for ch in s:
            if ch in pairs:  # 说明是右括号
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack



solu = Solution()
s = "()[]{}"
print(s[0])
print(s[1])
print(s[0]!=s[1])
ans = solu.isValid(s)
print(ans)


