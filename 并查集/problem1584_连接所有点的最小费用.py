"""
5513. 连接所有点的最小费用
给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。
请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
示例 1：
输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20
解释：
我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。

示例 2：
输入：points = [[3,12],[-2,5],[-4,1]]
输出：18

示例 3：
输入：points = [[0,0],[1,1],[1,0],[-1,1]]
输出：4

示例 4：
输入：points = [[-1000000,-1000000],[1000000,1000000]]
输出：4000000

示例 5：
输入：points = [[0,0]]
输出：0
提示：
1 <= points.length <= 1000
-106 <= xi, yi <= 106
所有点 (xi, yi) 两两不同。
"""
# 大概知道是最小生成树问题，但是并不知道如何进行编码，题解中使用的是并查集方法来做。
# Kruskal算法：对边权值从小到大排序，从最小边开算选择。不与已选择的边构成回路就要，否则不要。
# 用并查集实现，排序后，每次加入一条边，若此边的两个顶点的祖先节点相同，说明加入这条边会构成回路，所以要舍弃这条边
# 若不相同，则加入。
from typing import List
from collections import defaultdict
class UF:
    def __init__(self, n):
        self.parents = defaultdict(int)
        for i in range(n):
            self.parents[i] = i   # 一开始，所有的节点的父节点都是自己，即各点都可以看成一个独立的树

    def find(self, x):
        while x != self.parents[x]:
            x = self.parents[x]
        return x

    def connect(self, p, q):
        return self.parents[p] == self.parents[q]

    def union(self, p, q):
        if self.find(p) == self.find(q):
            return
        # 这里的意思就是，我们要把p，q合在一起，那么怎么才算合在一起呢，那就是一个节点的祖先节点是另一个节点的祖先节点
        # 他们共同祖先了，那么他们就在同一棵树了呀
        self.parents[self.find(p)] = self.find(q)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 1:
            return 0
        dic = defaultdict(int)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dic[(i, j)] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        res = sorted(dic.items(), key=lambda x: x[1])   # 对字典按边权值排序
        sumn = 0
        uf = UF(len(points))
        tmp = 0
        for i in range(len(res)):
            t1, t2 = res[i]
            x, y = t1
            if uf.find(x) != uf.find(y):   # 他们的祖先节点不是同一个，则还属于不同树
                tmp += 1
                sumn += t2
                if tmp == len(points) - 1: # 所有边都已经加入，最小树以生成。
                    return sumn
                uf.union(x, y)

