from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    ans = solu.maxArea(height)
    print(ans)