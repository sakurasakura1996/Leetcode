s = "sdkfj"
p = "sdk.*"

first_match = s and p[0] in {s[0],'.'}   # bool型，这里是看 p[0]是否在 s[0] 或者'.'都为true.  前面加上s确保s不为空
print(first_match)
first = True
if not first or first:
    ans = 1 or 2
print(ans)

print("--------")
shuzu32 = [0]*5
print(shuzu32)
shuzu32_2 = [2,3,4,5,7,4,5,2]
print(max(shuzu32_2))
s = "(())("
print(s[-1])

a = 3
print(1 <= a <= 4)

edges = [2,3]
edges.remove(2)
print(edges)

print("---test defaultdict")
a = [1, 3, 4, 4, 5]
from collections import defaultdict
b = defaultdict(list)
b[2] = 4
b[3] = [4]
print(b)

print("---test字典的更新update")
a = {1:3}
b = {2:4}
a.update(b)
print(a)
