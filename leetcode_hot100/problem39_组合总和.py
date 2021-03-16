"""
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
提示：
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
"""
# 第一直觉是回溯，然后需要注意数组中的数可以被重复的选取，还要注意重复结果
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrace(cur, num, path):
            # cur为已选择，num = sum(cur) path为待选择,首先写递归终止条件
            if num == target and cur not in ans:
                ans.append(cur.copy())
                return
            for i, item in enumerate(path):
                if num + item > target:
                    break
                cur.append(item)
                backtrace(cur, num+item, path[i:])
                cur.pop()

        backtrace([], 0, candidates)
        return ans

if __name__ == '__main__':
    solu = Solution()
    candidates = [2, 3, 5]
    target = 8
    ans = solu.combinationSum(candidates, target)
    print(ans)

