"""
632 最小区间
你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。
示例 1:
输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出: [20,24]
解释:
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
"""
# way1 自己写的代码过程，但是提交时间超时，感觉是前面的排序过程太耗时了
# from typing import List
# from collections import Counter
#
#
# class Solution:
#     def smallestRange(self, nums: List[List[int]]) -> List[int]:
#         nums_extend = []
#         nums_len = len(nums)
#         for col in range(nums_len):
#             nums_extend += [[n,col] for n in nums[col]]
#         nums_extend.sort()
#         nums = [nums_extend[i][0] for i in range(len(nums_extend))]
#         idx = [nums_extend[i][1] for i in range(len(nums_extend))]
#         left = 0
#         right = 0
#         ans = []
#         cur_qvjian = nums[-1] - nums[0] + 1
#         window = Counter()
#         while right < len(nums_extend):
#             window[idx[right]] += 1
#             right_char = nums[right]
#             right += 1
#             while all(map(lambda x: window[x] >= 1, range(nums_len))):
#                 if right_char - nums[left] < cur_qvjian:
#                     cur_qvjian = right_char - nums[left]
#                     ans = [nums[left], right_char]
#                 window[idx[left]] -= 1
#                 left += 1
#         return ans

# 在看了一个别人写的滑动窗口方法，我感觉我和他的复杂度应该是一样的啊，但是确实他的运行时间应该小于我
# way2 仔细分析这种写法，比我快的地方在于，下面这种写法，首先先找到首次符合条件的结果，然后再开始我们经常写的滑动窗口写法，这样的好处是
# 这时候判断只需要判断窗口的最左边的那个值出现次数是否大于1，而我上面写的 all(map(lambda x: window[x] >= 1需要一直判断，当题目中的k较大
# 时，那么我每次执行到这里，仅判断都需要进行k次，所以分析下来，我上面写的代码复杂度比下面的复杂度是高了的。
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
        # 题解中的code相当于先进行了一个初始化，从而省略了较多不可行解，简化滑动窗口方法
        for i in range(nums_len):
            if window[i] == 0:
                while window[i] == 0:
                    window[idx[right]] += 1
                    right += 1
        while window[idx[left]] > 1:
            window[idx[left]] -= 1
            left += 1
        minHead, minTail = nums[left], nums[right-1]

        while right < len(nums_extend):
            window[idx[right]] += 1
            while window[idx[left]] > 1:
                window[idx[left]] -= 1
                left += 1
            if nums[right] - nums[left] < minTail - minHead:
                minHead,minTail = nums[left], nums[right]
            right += 1
        return [minHead,minTail]

solu = Solution()
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
ans = solu.smallestRange(nums)
print(ans)
