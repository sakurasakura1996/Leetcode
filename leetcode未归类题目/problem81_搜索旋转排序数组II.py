from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 直接遍历当然可以解决该问题，但是显然题目要求并不是这个。
        # 这个题目是原来题目的提升，题目改为了nums数组中存在重复元素了，当然应该还是可以用二分查找来解决的。
        if not nums:
            return False
        n = len(nums)
        left = 0
        right = n - 1
        # 这道题重复元素的影响就在于， 我们之前用 nums[mid]和nums[0]来判断mid在左边还是右边，现在当nums[0] = nums[mid]时判断不了
        # 那么当 nums[mid] == nums[0]时，我们就 start ++即可

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid]:
                # 分不清到底是前面有序还是后面有序，我们这个时候直接将 left ++ 就可以了，这个想法还挺不错的。相当于去掉了一个干扰项
                # 而且对比 前面无重复的题目，这里从nums[0]变成了nums[left]要注意这里的区分。
                left += 1
                continue
            if nums[left] < nums[mid]:
                # target 在左前半部分
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 后半部分有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 0, 1, 1, 1]
    target = 0
    ans = solu.search(nums, target)
    print(ans)


