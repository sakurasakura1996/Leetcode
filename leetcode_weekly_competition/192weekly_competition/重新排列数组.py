from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0 for i in range(2*n)]
        for i in range(n):
            ans[2*i] = nums[i]
        for j in range(n, 2*n):
            ans[(j-n)*2+1] = nums[j]
        return ans


solu = Solution()
nums = [1,1,2,2]
s = 2
ans = solu.shuffle(nums, s)
print(ans)