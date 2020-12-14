"""
最大非负子序和
"""
class Solution:
    def maxNonNegativeSubArray(self, A):
        # 滑动窗口，窗口内的和最大且所有元素不能是负数
        ans = -1

        if not A:return ans
        n = len(A)
        left = 0
        right = 0
        window = 0
        while right < n:
            if A[right] < 0:
                left = right + 1
                right = left
                window = 0
            else:
                window += A[right]
                ans = max(ans, window)
                right += 1
        return ans

solu = Solution()
A = [-1, -2, -3, -4, -5, -6]
ans = solu.maxNonNegativeSubArray(A)
print(ans)
