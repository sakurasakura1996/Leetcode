import sys
if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    n = len(s)
    stack = []
    tmp = ""
    for i, ch in enumerate(s):
        if ch != "(" and ch != ")":
            tmp += ch
        elif ch == "(":
            if tmp:
                stack.append(tmp)
                tmp = ""
            stack.append(ch)
        elif ch == ")":
            if tmp:
                stack.append(tmp)
                tmp = ""
            # 接下来找到对应的左括号。
            temp = ""
            while stack[-1] != "(":
                temp += stack.pop()
            stack.pop()
            stack.append(temp)
    ans = ""
    while stack:
        ans = stack.pop() + ans
    print(ans)










