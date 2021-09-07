from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        cur = 1
        nxt = 1
        while nxt < n:
            if nums[nxt] == nums[nxt-1]:
                nxt += 1
            else:
                nums[cur] = nums[nxt]
                cur += 1
                nxt += 1
        return cur

if __name__ == '__main__':
    solu = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    ans = solu.removeDuplicates(nums)
    print(nums)
    print(ans)