from typing import List
from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 这个方法大概率超时了
        n = len(nums)
        if n < 2:
            return []
        nums.sort()
        nums_dict = defaultdict(list)
        for i, num in enumerate(nums):
            nums_dict[num].append(i)
        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                target = 0 - nums[i] - nums[j]
                if target >= nums[j]:
                    for k in range(j+1, n):
                        if k > j+1 and nums[k] == nums[k-1]:
                            continue
                        if nums[k] == target:
                            ans.append([nums[i], nums[j], nums[k]])
                else:
                     break
        return ans

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        # 上述时间复杂度最差还是三次方，我们能不能将为平方呢，用哈希结构存储信息然后减少复杂度
        # 卧槽，这就可以了，昨天搞了半天，今天随便写了下就过了。。。。
        n = len(nums)
        if n < 2:
            return []
        nums_dict = defaultdict(list)
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            nums_dict[num].append(i)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target = 0 - nums[i] - nums[j]
                if target in nums_dict:
                    for item in nums_dict[target]:
                        if item > i and item > j:
                            ans.append([nums[i], nums[j], nums[item]])
                            break
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [0, 0, 0, 0, 0]
    ans = solu.threeSum2(nums)
    print(ans)



