from typing import List
class Solution:
    # 要求使用常数空间，一趟扫描方法
    def sortColors(self, nums: List[int]) -> None:
        # 一趟扫描还没想到，两趟扫描倒是简单
        count0 = count1 = count2 = 0
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1
        for i in range(count0):
            nums[i] = 0
        for i in range(count0, count0+count1):
            nums[i] = 1
        for i in range(count0+count1, len(nums)):
            nums[i] = 2

    def sortColors2(self, nums: List[int]) -> None:
        # 两次遍历也可以不用上面那么麻烦，直接用指针，第一次遍历将所有的0放到前面，第二次遍历将所有的1放到中间，2就都在最后面了
        n = len(nums)
        p0, p2 = 0, n-1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
            i += 1



if __name__ == '__main__':
    solu = Solution()
    nums = [0]
    solu.sortColors2(nums)
    print(nums)