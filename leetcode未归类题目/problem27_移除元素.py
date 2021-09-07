from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        cur = 0
        for i in range(n):
            if nums[i] == val:
                continue
            else:
                nums[cur] = nums[i]
                cur += 1
        return cur


if __name__ == '__main__':
    solu = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    ans = solu.removeElement(nums, val)
    print(ans)