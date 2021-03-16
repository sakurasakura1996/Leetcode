from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == '__main__':
    solu = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    ans = solu.search(nums, target)
    print(ans)