from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        cur = 1
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                continue
            else:
                nums[cur] = nums[j]
                cur += 1
        return cur


if __name__ == '__main__':
    solu = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    ans = solu.removeDuplicates(nums)
    print(ans)