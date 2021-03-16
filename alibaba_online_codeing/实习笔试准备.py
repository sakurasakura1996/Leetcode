import sys

for line in sys.stdin:
    a = line.split()
    N, L = int(a[0]), int(a[1])
    for i in range(L, 101):
        if i % 2 == 0 and N % i == (0.5 * i):
            ans = [str(x) for x in range(N//i - i//2 + 1, N//i + i//2 + 1)]
            outpout = " ".join(ans).lstrip().rstrip()
            print(outpout)
            break
        elif i % 2 == 1 and N % i == 0:
            ans = [str(x) for x in range(N//i - i//2, N//i + i // 2 + 1)]
            outpout = " ".join(ans).strip()
            print(outpout)
            break
    print("No")
