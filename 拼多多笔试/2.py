import sys
from collections import Counter
N = int(sys.stdin.readline().strip())
poke = sys.stdin.readline().strip().split(" ")
# print(N)
# print(poke)
poke_counter = Counter(poke)
# 贪心策略，先把能出的出了，四张或者两张没有组合的, 不对，好像可以拆开啊，如果有两张牌的，可以拆成
# 单排和三张牌搭。
ans = 0
one = 0
two = 0
three = 0
four = 0
for key, value in poke_counter.items():
    if value == 1:
        one += 1
    elif value == 2:
        two += 1
    elif value == 3:
        three += 1
    else:
        four += 1

if three <= one:
    ans += (four + two + one)
elif three <= one + 2 * two:
    ans += four
    tmp = three - one
    if tmp % 2 == 0:
        ans += (2 * two - tmp) // 2
    else:
        ans += (2 * two - tmp)// 2 + 1
    ans += three
elif three <= one + 2 * two + 4 * four:
    tmp = three - one - 2 * two
    if tmp % 4 == 0:
        ans += (4 * four - tmp) // 4
    else:
        ans += (4 * four - tmp) // 4 + 1
    ans += three
else:
    ans += three
print(ans)


# if three >= one:
#     tmp = three - one
#     if tmp < 2 * two:
#         delta = (2 * two - tmp) // 2 + 1
#         ans += delta
#     ans += three
#     print(ans)
# else:
#     ans += one
#     ans += two
#     print(ans)