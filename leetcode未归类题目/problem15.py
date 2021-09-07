"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# from typing import List
# class Solution:
#     def threeSum(self, nums: List[int]):
#         if len(nums) < 3:
#             return []
#         dic = dict()
#         ans = []
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] in dic:
#                 dic[nums[i]].append(i)
#             else:
#                 dic[nums[i]] = [i]
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 cur = nums[i]+nums[j]
#                 if (0-cur) in dic:
#                     tmp = dic[0-cur]
#                     for p in range(len(tmp)):
#                         if tmp[p] > i and tmp[p] > j:
#                             ans.append([nums[i],nums[j], nums[tmp[p]]])
#         return ans

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

# 这道题真的不是看上去那么好做啊，或者说你太菜了


nums = [-1, 0, 1, 2, -1, -4]
solu = Solution()
ans = solu.threeSum(nums)
print(ans)
