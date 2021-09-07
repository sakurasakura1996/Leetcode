# 这个题目是二分查找的经典题目，二分查找除了查找某一个数，还有查找一个重复数的左边界和右边界。这里就是查找左边界和右边界
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        n = len(nums)
        # 查找左边界，如果没有返回-1，直接返回[-1, -1]
        left = 0
        right = n
        # 二分法的细节挺麻烦的，因为我这里right初始值为n，n取不到，说明我的搜索区间是左闭右开，所以如果left==right的时候，已经可以跳出循环了
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:     # 下面要注意，right到底怎么取值，到底是right=mid还是right=mid-1
                 right = mid
        if left == n or nums[left] != target:
            return [-1, -1]

        ans_left = left

        left = 0
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1    # 这一步要注意啊，为什么是加1呢
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid     # 这里又要注意了
        return [ans_left, left-1]


if __name__ == '__main__':
    solu = Solution()
    nums = [2, 2]
    target = 3
    ans = solu.searchRange(nums, target)
    print(ans)
