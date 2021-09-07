import sys
import math
if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    nums = sys.stdin.readline().strip().split()
    nums = [int(num) for num in nums]
    # print(math.sqrt(5))
    target = 0
    need = []
    ans = 0
    for num in nums:
        a = math.sqrt(num)
        if a == int(a) * int(a):
            target += 1
        else:
            temp = min(num-int(a)*int(a), (int(a)+1)*(int(a)+1)-num)
            need.append(temp)
    if target >= n // 2:
        print(ans)
    else:
        need.sort()
        for i in range(n//2-target):
            ans += need[i]
        print(ans)





