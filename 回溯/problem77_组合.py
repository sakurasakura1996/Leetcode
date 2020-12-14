"""
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
from typing import List


class Solution:
    def combine_2(self, n: int, k:int) -> List[List[int]]:
        # 回溯方法
        nums = [i for i in range(1, n+1)]
        ans = []

        def backtrack(cur, tmp):
            # cur为候选列表，tmp为已选择列表
            if len(tmp) == k:
                ans.append(tmp)
                return
            else:
                for idx, num in enumerate(cur):
                    backtrack(cur[idx+1:], tmp+[num])

        backtrack(nums, [])
        return ans


solu = Solution()
n = 4
k = 2
ans = solu.combine_2(n, k)
print(ans)
