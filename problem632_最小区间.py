"""
632. 最小区间
你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。
示例 1:
输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出: [20,24]
解释:
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
注意:
给定的列表可能包含重复元素，所以在这里升序表示 >= 。
1 <= k <= 3500
-105 <= 元素的值 <= 105
对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。
"""
# 难度为hard，这道题我以前在练习滑动窗口时还写出来了一个超时的代码
# 但是这次写的时候，我却没有想到用滑动窗口，而是想着用双指针，然后再结合二分搜索，双指针有点类似于滑动窗口
# 难受啊，做过的题还是写不出来，说明代码能力没跟上而且还是没有真正理解题目

from typing import List
from collections import Counter

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        nums_extend = []
        nums_len = len(nums)
        for col in range(nums_len):
            nums_extend += [[n,col] for n in nums[col]]
        nums_extend.sort()
        nums = [nums_extend[i][0] for i in range(len(nums_extend))]
        idx = [nums_extend[i][1] for i in range(len(nums_extend))]

        left = 0
        right = 0
        window = Counter()
        for i in range(nums_len):
            if window[i] == 0:
                while window[i] == 0:
                    window[idx[right]] += 1
                    right += 1
        while window[idx[left]] > 1:
            window[idx[left]] -= 1
            left += 1
        minHead, minTail = nums[left], nums[right-1]

        # 上面算是滑动窗口的简单初始化，下面才是滑动窗口的code
        while right < len(nums_extend):
            window[idx[right]] += 1
            while window[idx[left]] > 1:
                window[idx[left]] -= 1
                left += 1
            if nums[right] - nums[left] < minTail - minHead:
                minHead, minTail = nums[left], nums[right]
            right += 1
        return [minHead, minTail]