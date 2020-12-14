"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""
# 这道题相比problem704直接写二分查找代码，就是把数组由没有重复数字改成了有重复数字
# 二分查找理解起来不难，但是编码的细节需要多加注意，尤其时 +1 -1， 等于号是否需要，具体内容可以看Labuladong算法小抄，写的挺好
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        left1 = 0
        right1 = n
        left2 = 0
        right2 = n
        # 寻找左侧区间边界
        while left1 < right1:  # 二分查找这里有没有等于号就看你right的初始设置，也就是你查找到区间是左闭右开还是两端都闭，仔细理解这句话就懂了
            # 比如如果 right = n，那么证明搜索区间是左闭右开的，那么循环终止条件只要left == right就可以啦。因为[left, left)已经没有数了
            # left1 是为了寻找左边界
            mid = (left1 + right1) // 2
            if nums[mid] == target:
                right1 = mid    # 这里不需要-1，因为我这里用的有端是开区间，所以mid取不到，那么最大能取到的数也就是mid-1啦呀
            elif nums[mid] > target:
                right1 = mid
            elif nums[mid] < target:
                left1 = mid+1
        # 那么左侧边界应该就是left1 或者 right1,还是因为是左闭右开，循环终止条件就是left1 == right1了，所以返回谁都行啦

        # 寻找右侧区间
        while left2 < right2:
            mid = (left2 + right2) // 2
            if nums[mid] == target:
                left2 = mid + 1  # 左闭区间，所以
            elif nums[mid] > target:
                right2 = mid    # 右开区间啦
            elif nums[mid] < target:
                left2 = mid + 1
        # 这时候返回 left-1 才是右侧区间哦，因为上面第一个left2 = mid + 1时，我当时就有点疑惑，如果这个mid就是最右边的那个target,
        # 那left不是已经走过了吗，left = mid + 1为什么不行吗，首先，我们一定要直到，每一种情况下，区间一定是要往前行进的，如果区间没动那
        # 就会陷入没有执行任何操作的死循环之中啦。这里减一，是搜索右侧边界的一个特殊点。
        # if nums[left1] == target and nums[left2-1] == target: # 如果target在最右侧，那么会引起数组越界的情况，所以判断要加一些
        if left1 < n and nums[left1] == target and nums[left2-1] == target:
            return [left1,left2-1]
        else:
            return [-1, -1]

solu = Solution()
# nums = [5, 7, 7, 8, 8, 10]
# target = 8
nums = [2, 2]
target = 3
ans = solu.searchRange(nums, target)
print(ans)



