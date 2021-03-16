"""
剑指 Offer 56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
限制：
2 <= nums.length <= 10000
"""
# 这题目昨天还看到了，只不过我用了python中的数据结构Counter用笨方法解决了就跳过了。
# 现在这个方法，要求O(n)的时间复杂度，O(1)的空间复杂度，那还是需要好好思考
from typing import List
from collections import Counter
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)
        ans = []
        for key, value in nums_counter.items():
            if value == 1:
                ans.append(key)
        return ans

    def singleNumbers2(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        nums.sort()
        ans = []
        if nums[0] != nums[1]:
            ans.append(nums[0])
        if nums[-1] != nums[-2]:
            ans.append(nums[-1])
        for i in range(1, len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                ans.append(nums[i])
        return ans

    # 以上两种方法，第一种方法，空间复杂度并不是O（1），第二种方法因为排序，时间复杂度是O(nlogn),
    # 目前还没想到O（1）空间复杂度的方法，再想想
    def singleNumbers_3(self, nums: List[int]) -> List[int]:





if __name__ == '__main__':
    solu = Solution()
    nums = [3, 2, 1, 3]
    ans = solu.singleNumbers2(nums)
    print(ans)


