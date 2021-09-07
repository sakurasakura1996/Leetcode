from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        n = len(nums)
        nums.sort()
        ans = [[]]
        def backtrace(cur, path, l):
            if len(cur) == l:
                ans.append(cur.copy())
                return
            for i, value in enumerate(path):
                if i > 0 and path[i] == path[i-1]:
                    continue
                cur.append(value)
                temp = path[i+1:]
                backtrace(cur, temp, l)
                cur.pop()

        for i in range(1, n+1):
            backtrace([], nums, i)
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [0]
    ans = solu.subsetsWithDup(nums)
    print(ans)