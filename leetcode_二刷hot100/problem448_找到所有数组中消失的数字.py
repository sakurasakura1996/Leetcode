# 要求时间复杂度为O(n),空间复杂度为O(1),不算返回的数组
from typing import List
from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)
        ans = []
        for i in range(1, len(nums)+1):
            if i not in nums_counter:
                ans.append(i)
        return ans

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 就用nums来记录对应位置的数是否出现过
        n = len(nums)
        for num in nums:
            x = (num-1)%n
            nums[x] += n
        ans = [i+1 for i, num in enumerate(nums) if num <= n]
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [4,3,2,7,8,2,3,1]
    ans = solu.findDisappearedNumbers(nums)
    print(ans)

