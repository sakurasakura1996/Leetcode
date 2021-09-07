from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        num = 1
        cur = 1
        p = 1
        while p < n:
            if nums[p] != nums[p-1]:
                nums[cur] = nums[p]
                cur += 1
                p += 1
                num = 1
            elif nums[p] == nums[p-1] and num < 2:
                nums[cur] = nums[p]
                cur += 1
                p += 1
                num += 1
            else:
                p += 1
        return cur

if __name__ == '__main__':
    solu = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    ans = solu.removeDuplicates(nums)
    print(ans)


