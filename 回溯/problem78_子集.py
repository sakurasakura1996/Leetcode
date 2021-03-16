from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrace(cur, path):
            if len(cur) <= len(nums) and cur not in ans:
                ans.append(cur)

            for i, num in enumerate(path):
                cur.append(num)
                tmp = path[i+1:]
                backtrace(cur, tmp)
                cur.pop()

        backtrace([], nums)
        return ans
