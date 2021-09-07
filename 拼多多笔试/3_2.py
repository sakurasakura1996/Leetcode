import sys

line1 = sys.stdin.readline().strip().split(" ")
N, K = int(line1[0]), int(line1[1])
nums = sys.stdin.readline().strip().split(" ")
for i, num in enumerate(nums):
    nums[i] = int(num)

ans = 0
for i in range(N - K + 1):
    window = nums[i:i+K]
    window.sort()
    ans += window[(K-1)//2]

print(ans)
