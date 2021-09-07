from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()

        ans = []
        def backtrace(cur, path):
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            for i, value in enumerate(path):
                if i > 0 and value == path[i-1]:
                    continue
                cur.append(value)
                temp = path[:i]+path[i+1:]
                backtrace(cur, temp)
                cur.pop()
        backtrace([], nums)
        return ans

if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 3]
    ans =solu.permuteUnique(nums)
    print(ans)