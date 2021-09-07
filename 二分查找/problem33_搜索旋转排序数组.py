from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 这个题目主要就是考查这种情况下的二分查找怎么实现。题目简单点就是数组中数值各不相同，II就是有重复元素
        if not nums:
            return -1
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                # 那么其实这里的二分就是分成两个独立的区域进行二分查找嘛，思路和最基本的二分查找没什么区别啊。要把问题简单化
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:   # nums[mid] < target: 如果等于的话已经返回了，
                    left = mid + 1
            else:  # nums[0] > nums[mid] 说明mid 在右半部分，
                if nums[mid] < target <= nums[n-1]:
                    left = mid + 1
                else:  # target < nums[mid]
                    right = mid - 1
        return -1


if __name__ == '__main__':
    solu = Solution()
    nums = [1]
    target = 0
    ans = solu.search(nums, target)
    print(ans)
