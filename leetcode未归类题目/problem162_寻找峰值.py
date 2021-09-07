from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        for i in range(1, n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        return -1

    def findPeakElement2(self, nums: List[int]) -> int:
        # 迭代二分查找
        left = 0
        right = len(nums) - 1
        while left < right:   # 虽然上面right=n-1，但是这里不能取等号啊。
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]:  # 我们可以想想这里为什么不是 mid-1 而要是 mid+1呢,因为如果left=1，right=2的时候，mid会取
                # 左边的数，从而mid+1是有意义的，而mid-1无意义，所以不行啊。
                right = mid
            else:
                left = mid + 1
        return left

    def findPeakElement3(self, nums: List[int]) -> int:

        def getTop(nums, left, right):
            if left == right:
                return left
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
            return getTop(nums, left, right)
        return getTop(nums, 0, len(nums) - 1)



if __name__ == '__main__':
    solu = Solution()
    nums = [1,2]
    ans = solu.findPeakElement2(nums)
    print(ans)
