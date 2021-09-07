import sys
from collections import defaultdict

class Solution:
    def answer(self, m, relation):
        ans = 10
        visited = [0] * m  # 0 未访问   1 表示正在被访问   2 表示已经被访问了
        isHuan = False  # 是否存在环
        # 若存在循环，减两分, dfs, 访问到某个点如果没有依赖别人，则不记为访问过
        def dfs(i, number):
            nonlocal isHuan
            if visited[i] == 1:
                isHuan = True
                return
            elif visited[i] == 2:
                return
            else:
                if not relation[i] and number == 0:
                    # number = 0 表示自己访问自己的
                    visited[i] = -1
                    return
                else:
                    visited[i] = 1
                    for adj in relation[i]:
                        dfs(adj, 1)
                    visited[i] = 2

        for i in range(m):
            if visited[i] == 0:
                dfs(i, 0)

        if isHuan:
            ans -= 2
        for vis in visited:
            if ans > 0 and vis == -1:
                ans -= 1
        return ans


if __name__ == '__main__':
    m = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    relation = defaultdict(list)
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        a, b = int(line[0].strip()), int(line[1].strip())
        relation[a].append(b)
    # ans = 10
    # visited = [0] * m    # 0 未访问   1 表示正在被访问   2 表示已经被访问了
    # isHuan = False  # 是否存在环
    # 若存在循环，减两分, dfs, 访问到某个点如果没有依赖别人，则不记为访问过
    solu = Solution()
    ans = solu.answer(m, relation)
    print(ans)
    # def dfs(i, number):
    #     if visited[i] == 1:
    #         isHuan = True
    #         return
    #     elif visited[i] == 2:
    #         return
    #     else:
    #         if not relation[i] and number == 0:
    #             # number = 0 表示自己访问自己的
    #             visited[i] = -1
    #             return
    #         else:
    #             visited[i] = 1
    #             for adj in relation[i]:
    #                 dfs(adj, 1)
    #             visited[i] = 2
    #
    # for i in range(m):
    #     if visited[i] == 0:
    #         dfs(i, 0)
    #
    # if isHuan:
    #     ans -= 2
    # for vis in visited:
    #     if ans > 0 and vis == -1:
    #         ans -= 1
    # print(isHuan)
    # print(visited)
    # print(ans)







