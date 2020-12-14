"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
# 经典全排列题
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(nums, track):
            # nums为选择列表，track为路径列表
            if len(track) == len(nums):  # 表明已经到达决策树的叶节点了，这里不对nums数组进行删除和增加，而是遍历nums排除已经在track列表中的数字
                # ans.append(track)  这里极其容易出错，卧槽，因为后面的代码有执行track.pop()的操作，ans中的结果会随之pop()...
                ans.append(track.copy())
                return
            for num in nums:
                if num in track:
                    continue
                # 做出了选择
                track.append(num)
                # 进入下一层决策树
                backtrack(nums, track)
                # 取消选择
                track.pop()

        backtrack(nums, [])
        return ans

    def permute_2(self, nums: List[int]) -> List[List[int]]:
        # 完全同上面，这里只是重新再写一遍，熟悉熟悉
        ans = []

        def backtrack(nums, track):
            # nums为选择列表，track为路径列表
            if len(nums) == len(track):
                ans.append(track.copy())
                return
            for num in nums:
                if num in track:
                    continue
                track.append(num)
                backtrack(nums, track)
                track.pop()
        backtrack(nums, [])
        return ans


solu = Solution()
nums = [1, 2, 3]
ans = solu.permute(nums)
print(ans)