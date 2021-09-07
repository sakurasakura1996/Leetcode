from typing import List
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 思路就是维持不同任务的剩余个数，但是还要比较任务种类数和n的大小。
        if n == 0:
            return len(tasks)
        tasks = list(Counter(tasks).values())

        tasks.sort(reverse=True)
        ans = 0
        if len(tasks) <= n+1:
            ans = (tasks[0]-1)*(n+1)
            tasks = [num-tasks[0]+1 if (num-tasks[0]+1)>0 else 0 for num in tasks]
            ans += sum(tasks)
            return ans
        else:
            # 每次给最大的n+1个数减1
            while tasks[0] > 1:
                for i in range(n+1):
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
    ans = solu.leastInterval(tasks, n)
    print(ans)


