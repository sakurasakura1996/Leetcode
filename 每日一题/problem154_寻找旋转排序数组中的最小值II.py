from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 每日一题，今天太忙了，先O(n)复杂度通过再说
        ans = float('inf')
        for num in nums:
            if num < ans:
                ans = num
        return ans

    def findMin2(self, nums: List[int]) -> int:
        # 带有重复元素的二分法
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
        return nums[left]

    def findMin3(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] == nums[mid]:
                right -= 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

    def findMin4(self, nums: List[int]) -> int:
        """
        此处并不是解决上面的问题的，题目改成了，nums原来为降序数组，然后在某一个地方折断了，要你返回数组中最小的数
        """
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[left]:
                left += 1
            elif nums[mid] < nums[left]:
                left = mid
            else:
                right = mid - 1
        return nums[left]


if __name__ == '__main__':
    solu = Solution()
    nums = [5, 4, 3, 7, 6, 5]
    ans = solu.findMin4(nums)
    print(ans)

