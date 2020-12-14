"""
面试题 08.04. 幂集
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。
说明：解集不能包含重复的子集。
示例:
 输入： nums = [1,2,3]
 输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
from typing import List
from collections import deque
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 方法1：BFS方法
        if not nums:
            return [[]]
        nums.sort()
        queue = deque([(nums, [])])
        ans = []
        while queue:
            cur_nums, cur_ans = queue.popleft()
            if cur_ans not in ans:
                ans.append(cur_ans)

            for idx, i in enumerate(cur_nums):
                queue.append((cur_nums[idx+1:], cur_ans + [i]))
        return ans

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        # 方法二：回溯法 or DFS
        if not nums:
            return [[]]
        nums.sort()
        ans = []
        def backtrack(nums, tmp):
            ans.append(tmp)
            for idx, i in enumerate(nums):
                # 避免重复
                if idx > 0 and nums[idx] == nums[idx-1]:
                    continue
                backtrack(nums[idx+1:], tmp+[i])

        backtrack(nums, [])
        return ans


solu = Solution()
nums = [1, 2, 3]
ans = solu.subsets2(nums)
print(ans)




