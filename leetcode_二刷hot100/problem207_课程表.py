from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 看到这个题目就觉得挺难的啊呜呜呜。能想到的点就是，我们可不可以根据输入来组建起一个图来，然后搜索看看图中是否有环，如果有环的话，
        # 那么这个课程肯定是完不成的。一共有numCourses道题目，那我们能不能在数组的基础上维护一个记录某个课程学完可以学另外一门课程的记录呢
        if numCourses == 1:
            return True
        flags = [0] * numCourses
        records = defaultdict(list)
        # 这就是图的邻接表结构啊，大宝贝。。
        for prerequisite in prerequisites:
            cur, prev = prerequisite
            records[prev].append(cur)

        def dfs(i):
            if flags[i] == -1: # 表示节点被其他节点访问了
                return True
            if flags[i] == 1:  # 表示已经被当前节点访问了，在访问一次说明有环
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


if __name__ == '__main__':
    solu = Solution()
    numCourses = 4
    prerequistes = [[1,0],[2,0],[3,1],[3,2]]
    ans = solu.canFinish(numCourses, prerequistes)
    print(ans)








