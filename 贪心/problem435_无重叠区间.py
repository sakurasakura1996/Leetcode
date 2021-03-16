"""
435. 无重叠区间
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
注意:
可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:
输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:
输入: [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:
输入: [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
"""
# 这题虽然知道用贪心算法，但是还是不太会分析，看题解的思路之前，我想的是先按左侧元素大小排序，相同的再按照右侧元素排序。
# 然后，看后面的如果包含在前者的区间，则删除前者，如果后者包含前者，则后者，如果没有重叠则保留，如果有重叠则保留前者。
# 后面在解题过程中，还是可以用画图解来简化思考模式，其实总共就三种情况，用后面的区间不断从后往前平移就行了。

# 看了题解之后，我的方法还可以再简化一些，因为并不需要维护上一个区间的左右端点，仅仅是根据右端点就可以了啊。
# 这道题让我想到了之前汤老师大一C语言练习题中的一道题，也是用贪心，然后也是根据右端点排序就ok啦。
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() # 正好这个就是按照我们的想法再排序
        n = len(intervals)
        if n == 0:
            return 0
        ans = 0
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, n):
            cur_left = intervals[i][0]
            cur_right = intervals[i][1]
            if cur_left >= right:
                # 没有重叠
                left = cur_left
                right = cur_right
            elif cur_left < right and cur_right > right:
                ans += 1
            elif cur_left >= left and cur_right <= right:
                ans += 1
                left = cur_left
                right = cur_right
        return ans


    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        if not intervals:return 0

        intervals.sort(key=lambda x:x[1])  # 记住python对List[List[int]]的可选择性排序写法
        n = len(intervals)
        right = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]
        return n - ans


if __name__ == '__main__':
    solu = Solution()
    intervals = [[1,2], [2, 3]]
    ans = solu.eraseOverlapIntervals2(intervals)
    print(ans)
