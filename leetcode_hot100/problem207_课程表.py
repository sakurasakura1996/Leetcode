from typing import List
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS 方法来写，如果有环直接return False
        if numCourses == 1:
            return True
        records = defaultdict(list)
        for cur, prev in prerequisites:
            records[prev].append(cur)
        flags = [0] * numCourses

        def dfs(i):
            if flags[i] == -1:  # 表示前面已经访问过了，不用管了
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in records[i]:
                if not dfs(j):
                    return False
            flags[i] = -1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 再使用BFS来写写看
        if numCourses == 1:
            return True
        records = defaultdict(list)
        in_degrees = [0] * numCourses
        for cur, prev in prerequisites:
            records[prev].append(cur)
            in_degrees[cur] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        ans = 0
        while queue:
            node = queue.popleft()
            ans += 1    # 能访问到的节点数+1

            for i in records[node]:
                in_degrees[i] -= 1
                if in_degrees[i] == 0:
                    queue.append(i)
        if ans != numCourses:
            return False
        return True


if __name__ == '__main__':
    solu = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    ans = solu.canFinish2(numCourses, prerequisites)
    print(ans)
