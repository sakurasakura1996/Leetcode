"""

"""
from typing import List
from bisect import bisect_right

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        h = n // 2
        s = set()
        mask = 1 << h
        for i in range(mask):
            cur = 0
            for j in range(h):
                if i & 1 << j:
                    cur += nums[j]
            s.add(cur)
        res = sorted(s)
        lh = n - h
        mask = 1 << lh
        ans = inf
        for i in range(mask):
            b = 0
            for j in range(lh):
                if i & 1 << j:
                    b += nums[j + h]
            ind = bisect_right(res, goal - b)
            if ind:
                ans = min(ans, goal - b - res[ind - 1])
            if ind < len(res):
                ans = min(ans, res[ind] + b - goal)
        return ans
