from collections import defaultdict
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequistes: List[List[int]]) -> List[int]:
        ans = []  # 这道题和前一道题，代码上还是需要改改思路。
        records = defaultdict(list)
        flags = [0] * numCourses
        for prerequiste in prerequistes:
            cur, prev = prerequiste
            records[prev].append(cur)
        valid = True

        def dfs(i):
            nonlocal valid
            flags[i] = 1  # 搜索中的状态
            for j in records[i]:
                if flags[j] == 0:  # 未搜索
                    dfs(j)
                    if not valid:
                        return
                elif flags[j] == 1: # 搜索中，说明有环
                    valid = False
                    return
                # flags[j] = -1 说明该节点已经搜索完成，我们不用处理其他操作了。
            flags[i] = -1   # 已完成搜索
            ans.append(i)

        for i in range(numCourses):
            if valid and not flags[i]:
                dfs(i)
        if not valid:
            return []
        return ans[::-1]

    def findOrder2(self, numCourses: int, prerequistes: List[List[int]]) -> List[int]:
        # 这里再写一遍，主要上面的写法是官方题解中的写法，和课程表I这道题的写法不统一，我感觉记忆不太好，还是自己理解性的再写一遍
        ans = []  # 下面这部分数据的处理思路是一模一样的。
        records = defaultdict(list)
        flags = [0] * numCourses
        for prerequiste in prerequistes:
            cur, prev = prerequiste
            records[prev].append(cur)
        valid = True

        def dfs(i):
            nonlocal valid
            if flags[i] == -1:  # 已完成搜索，什么都不用管了
                return
            elif flags[i] == 1:   # 当前节点正在被访问，则说明有环了
                valid = False
            elif flags[i] == 0 and valid:
                # 未被访问过，
                flags[i] = 1
                for j in records[i]:
                    if valid:
                        dfs(j)
                flags[i] = -1
                ans.append(i)   # 我们当ans为栈结构，如果当前访问节点的字节点都已经遍历完了，那么当前节点再入栈，当然返回结果时倒序一下就行。
                return True

        for i in range(numCourses):
            if valid and not flags[i]:
                dfs(i)
        if not valid:
            return []
        return ans[::-1]

    def findOrder3(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 大佬题解中说这道题广度优先遍历更加经典啊，https://leetcode-cn.com/problems/course-schedule-ii/solution/tuo-bu-pai-xu-shen-du-you-xian-bian-li-python-dai-/
        # 广度优先从入度为0的节点开始遍历，先将入度为0的节点放入队列中，只要队列非空，就从队首取出入度为0的节点，将这个节点输出到结果中去。并且将
        # 该节点的所有邻接节点的入度减1，在减1之后，如果入度变为0，则将其放入队列中。当队列为空时，检查结果集中的顶点个数是否和课程数相等即可
        in_degrees = [0 for _ in range(numCourses)]  # 入度数组，一开始全部为0
        # 邻接表
        adj = [set() for _ in range(numCourses)]
        for cur, prev in prerequistes:
            in_degrees[cur] += 1
            adj[prev].add(cur)

        # 首先遍历一遍，把所有入度为 0 的节点加入队列
        ans = []
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        while queue:
            top = queue.pop(0)
            ans.append(top)

            for nxt in adj[top]:
                in_degrees[nxt] -= 1
                if in_degrees[nxt] == 0:
                    queue.append(nxt)
        if len(ans) != numCourses:
            return []
        return ans




if __name__ == '__main__':
    solu = Solution()
    numCourses = 2
    prerequistes = [[1,0]]
    ans = solu.findOrder3(numCourses, prerequistes)
    print(ans)