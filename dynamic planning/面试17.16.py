"""
面试题17.16 按摩师
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约
请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。
注意：本题相对原题稍作改动

示例 1：
输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
"""
from typing import List
class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_len = len(nums)
        if nums_len <= 2:
            return max(nums)
        ans = [0] * nums_len
        ans[0] = nums[0]
        ans[1] = max(nums[0:2])
        for i in range(2, nums_len):
            ans[i] = max(ans[i-1], ans[i-2]+nums[i])
        return ans[nums_len-1]
solu = Solution()
nums = [2,1,4,5,3,1,1,3]
ans = solu.massage(nums)
print(ans)


