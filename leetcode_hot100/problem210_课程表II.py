from typing import List
from collections import defaultdict, deque
class Solution:
    # 我们用DFS和BFS各写一遍，熟能生巧
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 先用BFS 来做，因为确实拓扑排序，BFS应该更合适些。
        records = defaultdict(list)
        in_degrees = [0] * numCourses

        for cur, prev in prerequisites:
            records[prev].append(cur)
            in_degrees[cur] += 1

        queue = deque()
        ans = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            ans.append(node)

            for i in records[node]:
                in_degrees[i] -= 1
                if in_degrees[i] == 0:
                    queue.append(i)
        if len(ans) != numCourses:
            return []
        return ans

    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 使用DFS来写，我们要用栈来存储访问的节点顺序，比如，访问到A节点，如果A节点的相邻节点（这里指从A节点出发到达的节点）都已经访问了，那么
        # A 节点再入栈，这时候那些节点都已经入栈了。
        records = defaultdict(list)
        for cur, prev in prerequisites:
            records[prev].append(cur)
        valid = True   # valid表示
        flags = [0] * numCourses
        ans = []

        # 注意valid是一个全局变量，我们最好保证dfs函数中，每dfs一个节点之后，访问下一个节点的时候都判断下valid是否是False，如果是就不用再麻烦了。

        def dfs(i):
            nonlocal valid
            if flags[i] == 1:
                valid = False
                return
            if valid and flags[i] == -1:
                valid = True  # 怎么能就这样判断valid=True，如果之前已经是False了，而且你前面还没有判断valid是否已经是False了啊
                return
            flags[i] = 1
            for j in records[i]:
                if valid:
                    dfs(j)
            flags[i] = -1
            ans.append(i)
            return True   # 我在leetcode提交，这里改成return，慢很多，return True快很多，这是为啥。

        for i in range(numCourses):
            if valid and not flags[i]:
                dfs(i)
        if not valid:
            return []
        return ans[::-1]


if __name__ == '__main__':
    solu = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    ans = solu.findOrder2(numCourses, prerequisites)
    print(ans)