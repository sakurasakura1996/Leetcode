s = "sdkfj"
p = "sdk.*"

first_match = s and p[0] in {s[0],'.'}   # bool型，这里是看 p[0]是否在 s[0] 或者'.'都为true.  前面加上s确保s不为空
print(first_match)
first = True
if not first or first:
    ans = 1 or 2
print(ans)
