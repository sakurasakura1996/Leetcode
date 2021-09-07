"""
785.判断二分图
给定一个无向图graph，当这个图为二分图时返回true。
如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。
这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。
示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释:
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释:
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。

注意:
graph 的长度范围为 [1, 100]。
graph[i] 中的元素的范围为 [0, graph.length - 1]。
graph[i] 不会包含 i 或者有重复的值。
图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。
"""
# 这道题研一的算法课上应该讲过的啊，可惜自己没什么印象。题解中使用的是BFS或者DFS方法来写，BFS还是挺熟悉的，因为写二叉树的层次遍历次数较多
# 这道题还是BFS更好理解，但其实本质都是一样的，因为都是染色问题，也就是把整个图进行遍历，那么DFS和BFS都一样的。我们可以从任意节点开始，把该节点
# 染色为红色，然后把该节点相邻染色成绿色，再将这些绿色节点依次遍历，和他们相邻的节点在染成红色，依次下去，如果出现相邻节点已经染色，而且准备对其染色
# 的颜色矛盾，则直接返回False，不能组成二分图，最后执行完都没返回的话，那就返回True
from typing import List
class Solution:
    def isBipartite_BFS(self, graph: List[List[int]]) -> bool:
        # 采用BFS方法来遍历
        from collections import deque
        graph_len = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2  # 给图中节点赋予三种状态
        color = [UNCOLORED] * graph_len

        for i in range(graph_len):
            if color[i] == UNCOLORED:
                q = deque([i])
                color[i] = RED
                while q:
                    node = q.popleft()
                    color_tmp = GREEN if color[node] == RED else RED
                    # 和node节点相邻的节点都要染色为color_tmp
                    for neighbor in graph[node]:
                        if color[neighbor] == UNCOLORED:
                            color[neighbor] = color_tmp
                            q.append(neighbor)
                        elif color[neighbor] != color_tmp:
                            return False
        return True

    def isBipartite_DFS(self, graph: List[List[int]]) -> bool:
        # 采用DFS的遍历方法来写这道题目，并且DFS的编码还不是很熟悉啊
        graph_len = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * graph_len
        valid = True

        def dfs(node:int, c:int):
            nonlocal valid   # nonlocal 区别于 global，nonlocal表示的是该变量是外部的局部变量，而global声明的是全局变量
            color[node] = c
            color_tmp = GREEN if c == RED else RED
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    dfs(neighbor,color_tmp)
                    if not valid:
                        return
                elif color[neighbor] != color_tmp:
                    valid = False
                    return

        for i in range(graph_len):
            if color[i] == UNCOLORED:
                dfs(i, RED)
                if not valid:
                    break
        return valid


if __name__ == '__main__':
    solu = Solution()
    graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
    ans = solu.isBipartite_DFS(graph)
    print(ans)













