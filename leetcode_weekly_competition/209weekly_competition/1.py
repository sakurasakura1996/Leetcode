from typing import List
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        lower = 0
        upper = nums[0]
        for i in range(n-1):
            cur = n - i
            if cur > lower and cur <= upper:
                return cur
            lower = nums[i]
            upper = nums[i+1]
        return -1

solu = Solution()
nums = [3,5]
ans = solu.specialArray(nums)
print(ans)