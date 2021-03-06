"""
207. 课程表
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
示例 1:
输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:
输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
提示：
输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5
"""
# 这道题貌似是在考察图，如果形成了环，那么就直接不能完成学习，如果没有环
# 还要计算所学的课程数量是不是超过了边界，超过了也不能完成学习。
# 那么检验是否有环的方法可以用DFS吧。用visited数组记录已经访问过的。搞了半天感觉还是不够熟悉啊
# 题解思路：
# 本题是一道经典的 拓扑排序 问题
# 给定一个包含n个节点的有向图G，我们给出它的节点编号的一种排列，如果满足：
# 对于图G中任意一条有向边（u，v），u在排列中都出现在v的前面那么称该排列是图G的 拓扑排序。根据上述的定义，我们可以得出两个结论：
#   1.如果图G中存在环，即如果该图不是有向无环图，那么图G不存在拓扑排序，这是因为假设图中存在环 x1,x2,...xn,x1，那么x1在排列中必须出现在xn
#     的前面，但xn同时也必须出现在x1的前面，因此不存在一个满足要求的排列，也就不存在拓扑排序
#   2.如果图G是有向无环图，那么它的拓扑排序可能不止一种。举一个最极端的例子，如果图G值包含n个节点却没有任何边，那么任意一种编号的排列都可以作为
#     拓扑排序。
# 有了上述的分析，我们可以将本题建模成一个求拓扑排序的问题了
# 我们将每一门课看成一个节点，学习课程A之前必须完成B，那么从B到A有一条有向边，这样在拓扑排序中，B一定出现在A的前面
# 求出该图是否存在拓扑排序，就可以判断是否有一种符合要求的课程学习顺序。
# 这道题和210 课程表II几乎相同，只不过输出不一样。求出一种拓扑排序的最有时间复杂度为O(n+m)，其中n和m分别是有向图G的节点数和边数。而判断图G
# 是否存在拓扑排序至少也要对其进行一次完整的遍历，时间复杂度也是O(n+m)
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 原理是通过DFS判断图中是否有环，有向图中判断是否有环，就是DFS的时候重复发现一个节点两次被当前节点访问了，这就说明有环了
        def dfs(i, adjacency, flags):
            if flags[i] == -1:return True   # -1表示访问节点已被其他节点启动的DFS访问，无需再重复搜索。直接返回True
            if flags[i] == 1:return False   # 1表示访问节点在本轮DFS搜索中第二次被访问，那么有向图有环，直接返回False
            flags[i] = 1  # 标记为该节点被本轮DFS访问过
            for j in adjacency[i]:  # 遍历访问当前节点i的所有邻接节点j，当发现环直接返回False
                if not dfs(j, adjacency, flags):return False
            flags[i] = -1   # 当前节点所有邻接节点已经被遍历，并没有发现环，则将当前节点flag置为-1，置为-1是方便给下一轮节点的DFS访问使用
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):return False
        return True









