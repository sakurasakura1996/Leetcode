"""
1004.最大连续1的个数 III
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
返回仅包含 1 的最长（连续）子数组的长度。
示例 1：
输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
"""
from typing import List
from collections import Counter
# class Solution:
#     def maxlianxv(self, A: List[int]) -> int:
#         ans = 0
#         tmp = 0
#         for i in range(len(A)):
#             if A[i] == 1:
#                 tmp += 1
#                 ans = max(ans, tmp)
#             else:
#                 tmp = 0
#         return ans
#
#     def longestOnes(self, A: List[int], K: int) -> int:
#         if Counter(A)[0] <= K:
#             return len(A)
#         if K == 0:
#             return self.maxlianxv(A)
#         left = 0
#         right = 0
#         window = Counter()
#         ans = 0
#         while right < len(A):
#             window[A[right]] += 1
#             right += 1
#             while window[0] == K:
#                 if right < len(A) and A[right] == 1:
#                     break
#                 else:
#                     if right - left > ans:
#                         ans = right -left
#                     window[A[left]] -= 1
#                     left += 1
#         return ans

# 第二天又来看了一下，发现完全不用想的那么复杂啊，虽然最后通过的用时还比上面那个用时久
# 思路就是，如果window[0] > k了，那肯定A[right]=0，那么我们将left++，直到又满足条件

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        right =0
        window = Counter()
        ans = 0
        while right < len(A):
            window[A[right]] += 1

            while window[0] > K:
                window[A[left]] -= 1
                left += 1
            right += 1
            ans = max(ans, right-left)
        return ans

# 上面这题难度不大，但是开始一直没有A过，主要是有几种情况不符合自己的思考思路，我是单独列出来然后
# 求解的，有时间去看下题解别人的统一解法
solu = Solution()
A = [0,0,1,1,1,0,0]
K = 0
ans = solu.longestOnes(A,K)
print(ans)



