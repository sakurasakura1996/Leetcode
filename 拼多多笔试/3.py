import sys

line1 = sys.stdin.readline().strip().split(" ")
N, K = int(line1[0]), int(line1[1])
nums = sys.stdin.readline().strip().split(" ")
for i, num in enumerate(nums):
    nums[i] = int(num)


window = nums[0:K]
window.sort()
ans = 0
ans += window[K//2]
for i in range(K, N):


