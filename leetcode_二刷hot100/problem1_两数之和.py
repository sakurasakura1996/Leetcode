from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_table = defaultdict(list)
        for i in range(n):
            hash_table[nums[i]].append(i)
        for i in range(n):
            if (target - nums[i]) in hash_table:
                for item in hash_table[target-nums[i]]:
                    if item != i:
                        return [i, item]
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # 上面的方法写的太拖拉
        hash_table = dict()
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target-num], i]
            hash_table[nums[i]] = i
        return []


if __name__ == '__main__':
    solu = Solution()
    nums = [3,2,4]
    target = 6
    ans = solu.towSum(nums, target)
    print(ans)
