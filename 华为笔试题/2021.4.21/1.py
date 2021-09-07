import sys
if __name__ == '__main__':
    line = sys.stdin.readline().strip().split()
    n, m = int(line[0].strip()), int(line[1].strip())
    A = []
    L = []
    C = []
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        A.append(int(line[0].strip()))
        L.append(int(line[1].strip()))
        C.append(int(line[2].strip()))
    seats = [m] * 24
    ans = [0] * 24
    for i in range(len(A)):
        a = A[i]
        l = L[i]
        c = C[i]
        flag = True
        for j in range(a, l):
            if seats[j] < c:
                flag = False
                break
        if flag:
            for j in range(a, l):
                seats[j] -= c
                ans[j] += c
    for num in ans:
        print(num, end=' ')






