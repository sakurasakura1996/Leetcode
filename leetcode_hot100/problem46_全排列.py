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
# 尤其注意这里的问题是没有重复数字的序列
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrace(cur, path):
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            for num in cur:
                if num in path:
                    continue
                path.append(num)
                backtrace(cur, path)
                path.pop()

        backtrace(nums, [])
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 2]
    ans = solu.permute(nums)
    print(ans)