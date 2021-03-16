# 第一反应是想用回溯法来实现该问题。
from typing import List
import sys
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        # 回溯法超时了。。
        self.ans = sys.maxsize

        def backtrace(cur: List[int], path: List[int], summ: int, goal: int):
            tmp = abs(summ-goal)
            if tmp < self.ans:
                self.ans = tmp
            for i, num in enumerate(cur):
                if num > 0 and summ > goal:
                    # 没必要再进行下去了啊。
                    return
                summ += num
                path.append(num)
                temp_cur = cur[:i] + cur[i+1:]
                backtrace(temp_cur, path, summ, goal)
                path.pop()
                summ -= num
        nums.sort()
        backtrace(nums, [], 0, goal)
        return self.ans


if __name__ == '__main__':
    solu = Solution()
    nums = [5,-7,3,5]
    goal = 6
    ans = solu.minAbsDifference(nums, goal)
    print(ans)
