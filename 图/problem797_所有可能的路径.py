from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # DFS 应该可以解决该问题啊，baby。
        ans = []
        n = len(graph)

        def backtrace(i, path):
            if i == n-1:
                ans.append(path.copy())
                return

            for j in graph[i]:
                path.append(j)
                backtrace(j, path)
                path.pop()

        backtrace(0, [0])
        return ans

if __name__ == '__main__':
    solu = Solution()
    graph = [[1,3],[2],[3],[]]
    ans =solu.allPathsSourceTarget(graph)
    print(ans)


