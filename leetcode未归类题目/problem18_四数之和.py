from typing import List
from collections import defaultdict
class Solution:
    # 这种题，我们如果四个for循环的话，应该会超时，nums长度最大为200，三次方应该还能通过
    # 确实通过了，但是效率很低。
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        nums_dict = defaultdict(list)
        for i, num in enumerate(nums):
            nums_dict[num].append(i)
        ans = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, n-1):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    cur = target - nums[i] - nums[j] - nums[k]
                    for item in nums_dict[cur]:
                        if item > k:
                            ans.append([nums[i], nums[j], nums[k], nums[item]])
                            break
        return ans

    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        # 相似的三数之和题目使用了 排序加双指针的思路，这里同样可以
        n = len(nums)
        if n < 4:
            return []

        nums.sort()
        ans = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = n-1
                cur_target = target - nums[i] - nums[j]
                while left < right:
                    if nums[left] + nums[right] == cur_target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while left + 1 < right and nums[left+1] == nums[left]:
                            left += 1
                        left += 1
                        while right - 1 > left and nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1
                    elif nums[left] + nums[right] < cur_target:
                        left += 1
                    elif nums[left] + nums[right] > cur_target:
                        right -= 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    ans = solu.fourSum2(nums, target)
    print(ans)

