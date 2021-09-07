class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        if s[0] == '+' or '-':
