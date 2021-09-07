from typing import List
class Solution:
# 这道题的方法有很多，都是很经典的解法，多关注这道题啊。
    def trap(self, height: List[int]) -> int:
        # 找到每个位置的左右的最大值, 使用动态规划将每次遍历的复杂度O(N^2)降到 O(N)。
        if not height:
            return 0
        n = len(height)
        leftMax = [height[0] + [0] * (n - 1)]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])

        rightMaX = [0] * (n - 1) + [height[n-1]]
        for i in range(n-2, -1, -1):
            rightMaX[i] = max(rightMaX[i+1], height[i])

        ans = sum(min(leftMax[i], rightMaX[i]) - height[i] for i in range(n))
        return ans

    def trap2(self, height: List[int]) -> int:
        # 单调栈解法：我们维护一个单调栈，存储的是下标，满足从栈底到栈顶的下标对应的数组height中的元素递减
        ans = 0
        stack = list()
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)
        return ans

    def trap3(self, height: List[int]) -> int:
        # 方法一，使用动态规划的策略存储了每个节点的左右最大值，这使用了一定的内存空间，那么可以不用O(N)的空间复杂度吗，可以，双指针能够实习那
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans




