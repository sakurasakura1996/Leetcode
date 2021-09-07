from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num], i]
            hashtable[num] = i

if __name__ == '__main__':
    solu = Solution()
    nums = [3, 2, 4]
    target = 6
    ans = solu.twoSum(nums, target)
    print(ans)
