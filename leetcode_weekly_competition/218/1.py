class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        n = len(command)
        start = 0
        while start < n:
            if command[start] == 'G':
                ans.append("G")
                start += 1
            elif command[start] == '(' and command[start+1] == ')':
                ans.append("o")
                start += 2
            elif command[start] == '(' and command[start+1] == 'a':
                ans.append("al")
                start += 4
        return "".join(ans)
