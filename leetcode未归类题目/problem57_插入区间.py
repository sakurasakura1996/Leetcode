from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        n = len(intervals)

        left = newInterval[0]
        right = newInterval[1]
        for interval_left, interval_right in intervals:
            if left > interval_right:
                continue
            elif interval_left <= left <= interval_right:
                if right <= interval_right:
                    continue
                else:

