import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    a = sys.stdin.readline().strip().split()
    b = sys.stdin.readline().strip().split()
    a = [int(num) for num in a]
    b = [int(num) for num in b]
    if n < 3:
        print(-1)
    record = []
    for i in range(n-1):
        temp = []
        for j in range(i+1, n):
            if a[i] < a[j]:
                temp.append(j)
        record.append(temp.copy())
    print(record)
    ans = float('inf')
    for i in range(n-2):
        temp = record[i]
        if not temp:
            continue
        for j in temp:
            if j > n-2:
                break
            temp2 = record[j]
            if not temp2:
                continue
            for k in temp2:
                ans = min(ans, b[i]+b[j]+b[k])
                # print(i, j, k)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)


# 8
# 9 8 6 7 7 2 9 2
# 9 1 10 8 6 4 8 6
# 24