"""
621. 任务调度器
给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都
可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
你需要计算完成所有任务所需要的 最短时间 。
示例 1：
输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。

示例 2：
输入：tasks = ["A","A","A","B","B","B"], n = 0
输出：6
解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
诸如此类

示例 3：
输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
输出：16
解释：一种可能的解决方案是：
     A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A
提示：
1 <= task.length <= 104
tasks[i] 是大写英文字母
n 的取值范围为 [0, 100]
"""
from typing import List
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n:int) -> int:
        if n == 0:
            return len(tasks)
        tasks = list(Counter(tasks).values())
        print(tasks)

        def answer(nums: List[int], n: int):
            nums.sort(reverse=True)
            ans = 0
            if len(nums) <= (n+1):
                ans = (nums[0]-1) * (n+1)
                nums = [num - nums[0] + 1 if (num - nums[0] + 1) > 0 else 0 for num in nums]
                ans += sum(nums)
                return ans
            else:
                # 如果nums的种类大于 n+1,我们每次给最大的n+1个数减1
                while nums[0] > 1:
                    for i in range(n+1):
                        if nums[i] > 0:
                            nums[i] -= 1
                    ans += (n+1)
                    nums.sort(reverse=True)
                ans += sum(nums)
                return ans

        ans = answer(tasks, n)
        return ans

    def leastInterval2(self, tasks: List[str], n:int) -> int:
        # 写完上面的写法，好像可以简单点
        if n == 0:
            return len(tasks)
        tasks = list(Counter(tasks).values())
        tasks.sort(reverse=True)
        ans = 0
        while tasks[0] > 1:
            for i in range(min(n+1, len(tasks))):
                if tasks[i] > 0:
                    tasks[i] -= 1
            ans += (n+1)
            tasks.sort(reverse=True)
        ans += sum(tasks)
        return ans


if __name__ == '__main__':
    solu = Solution()
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    ans = solu.leastInterval2(tasks, n)
    print(ans)