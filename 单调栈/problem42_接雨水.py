"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9
提示：
n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
"""
# 在做了84题，再来看这道题就感觉难度降了一点了。如果从每根柱子的高度角度考虑，那么每根柱子的蓄水量需要根据
# 其左右比它高的柱子中最高的柱子决定。那么如何分别找出该柱子左侧的最高柱子呢，递减栈是否可行，但是递减栈的
# 性质貌似是可以找到左起第一个比当前数字大的元素，那这也不符合我们的想法啊。但是好像也是可以的。我们自己先试试。
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = list()
        n = len(height)

        if n <= 0:
            return 0
        left, right = [0] * n, [0] * n

        for i in range(n):
            # stack里面得存储height数值的索引
            while stack and height[stack[-1]] <= height[i]:
                stack.pop()
            left[i] = stack[0] if stack else i
            stack.append(i)

        stack = list()
        for i in range(n-1, -1, -1):
            while stack and height[stack[-1]] <= height[i]:
                stack.pop()
            right[i] = stack[0] if stack else i
            stack.append(i)

        ans = 0
        for i in range(n):
            water = min(height[left[i]], height[right[i]]) - height[i]
            ans += water
        return ans

    def trap2(self, height: List[int]) -> int:
        # 看了题解，感觉大可不必用上面的单调栈什么的，说到底其实思路还是一个，如果按列计算的话，我们要求出这一列左边最大和右边最大的列的高度。
        # 但是为了遍历到一列时，我们不必每次都要重新遍历一遍它左边右边的最高值，我们可以一次遍历存储起来。其实也就是上面解法中的left和right数组
        # 这其中可以使用动态规划的思想来求的这两个数组。
        n = len(height)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            left[i] = max(left[i-1], height[i-1])

        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])

        ans = 0
        for i in range(1, n):
            water = min(left[i], right[i]) - height[i]
            ans += water if water > 0 else 0
        return ans
    # 思路和解法一其实基本相同，因为他们最初的出发点都还是一样的，按行求或者按列求。


solu = Solution()
height = [4,2,0,3,2,5]
ans = solu.trap2(height)
print(ans)

