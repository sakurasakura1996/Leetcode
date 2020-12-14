"""
40. 组合总和 II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""
from typing import List
from collections import deque
class Solution:
    # 仔细体会下面两种很通常的解法，方法一是BFS，方法二是回溯 or DFS方法。
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()   # 这里如果不排序的话，会有重复结果比如 [1,7] 和 [7,1]这是不允许的。
        n = len(candidates)
        queue = deque([(candidates, [], 0)])
        while queue:
            nums, track, cur_sum = queue.popleft()

            if cur_sum == target and track not in ans:
                ans.append(track)
            if cur_sum < target:
                for idx, i in enumerate(nums):
                    if cur_sum + i <= target:
                        queue.append((nums[idx+1:], track+[i], cur_sum+i))
        return ans

    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(candidates, tmp):
            if sum(tmp) > target:
                return
            if sum(tmp) == target:
                ans.append(tmp)
                return

            for i in range(len(candidates)):
                # 同样这里要注意避免重复结果，比如[2,2,3]这里，如果第二个2的结果完全可以忽略，因为前一个2的结果肯定会包括第二个2的结果。
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                backtrack(candidates[i+1:], tmp + [candidates[i]])
            return ans
        return backtrack(candidates, [])



solu = Solution()
candidates = [2,5,2,1,2]
target = 5
ans = solu.combinationSum3(candidates, target)
print(ans)


