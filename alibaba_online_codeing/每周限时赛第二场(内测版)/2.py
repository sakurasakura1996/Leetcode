"""
第二直径
描述
给出由n个结点，n-1条边组成的一棵树。求这棵树的第二直径，也就是两两点对之间距离的次大值。
给出大小为(n-1)*3的数组edge,edge[i][0],edge[i][1],edge[i][2],表示第i条边是从edge[i][0]连向edge[i][1]，长度为edge[i][2]的无向边。
2 <= n <= 100000
1 <= edge[i][2] <= 100000
因为DFS(Depth-First-Search)容易爆栈，请使用BFS(Breadth First Search)完成该题目

示例
输入:[[0,1,4],[0,2,7]]
输出:7
解释:两两之间的次大值为0到2的7
"""
# 求树的第一直径
#   * 从任意点P出发，找离他最远的Q，再从Q出发，找离他最远的W，W到Q的简单路径便是直径
#   证明： * 若P在路径上，那么根据直径定义，Q也在直径上，而且Q为直径的一个端点
#         * 若P不在直径上，假设WQ不是直径，AB是直径
# 求树的第二直径
# 本题要求我们求出树的第二直径也就是两两点对之间距离的次大值
# 那我们可以先忽略掉第一直径的值，再求两两点对之间的距离的最大值便是答案
#
# 先求出树的第一直径的两个端点，两个端点分别遍历整个树，算出每个点i到两个端点的距离distanceOne_i,distanceTwo_i
# 由上述证明的性质知道了到i的最远点一定是直径端点之一 那么maxDistance_i=max(distanceOne_i,distanceTwo_i)
# 忽略掉第一直径的值，再求两两点对之间的距离的最大值便是答案,那只需要我们遍历一遍，算出max(maxDistance_i ) 要求i不是第一直径的端点，就可以找出第二直径的答案了
# 复杂度分析
# 时间复杂度
# 令N为点数，从P出发遍历一遍找出Q的时间复杂度O(N),从Q出发遍历一遍找出W并计算出distanceOne的时间复杂度O(N),从W出发遍历一遍算出distanceTwo的时间复杂度O(N)
# 最后遍历一遍非直径端点的点，统计答案，所以最终的时间复杂度是O(N)
#
# 空间复杂度
# 令N为点数，遍历时需要distance距离数组，visited访问数组，queue bfs的队列，以及Edge树的边，所以空间复杂度O(N)
import collections
class Solution:
    """
       从begin点开始bfs遍历整个树，并计算出begin到每个点的距离 存到distance数组里
    """

    def bfs(self, begin, n, distance, pointEdge):

        # bfs队列
        deque = collections.deque()
        # 标记访问数组
        visited = [False] * n

        # 将begin压入队列
        distance[begin] = 0
        visited[begin] = True
        deque.append(begin)
        while (len(deque)):
            # 取出队首
            now = deque.popleft()

            # 枚举和now相连的其他点
            for i in range(len(pointEdge[now])):
                to = pointEdge[now][i][0]
                # print(to)
                value = pointEdge[now][i][1]
                # 如果相连的点没有访问过，则压入队列
                if visited[to] == False:
                    visited[to] = True
                    distance[to] = distance[now] + value
                    deque.append(to)

    """
        从distance数组里找出距离最大的位置
    """

    def findMaxDistanceIndex(self, distance):

        # 初始化最大距离和最大距离所在的数组下标
        maxDistance = 0
        index = 0

        # 找出最大距离
        for i in range(len(distance)):
            if distance[i] > maxDistance:
                maxDistance = distance[i]
                index = i

        return index

    """
       @param edge: edge[i][0] [1] [2]  start point,end point,value
       @return: return the second diameter length of the tree
    """

    def getSecondDiameter(self, edge):
        # write your code here

        # 边的数量
        edgeNumber = len(edge)

        # 点的数量
        n = edgeNumber + 1

        # 距离指定起点的距离
        distance = [0] * n
        # 距离直径第一个端点的距离
        distanceOne = [0] * n
        # 距离直径第二个端点的距离
        distanceTwo = [0] * n
        # 每个点储存有哪些边
        pointEdge = [[] for i in range(n)]

        # 加无向边

        for i in range(edgeNumber):
            pointEdge[edge[i][0]].append((edge[i][1], edge[i][2]))
            pointEdge[edge[i][1]].append((edge[i][0], edge[i][2]))

        # print(pointEdge)

        # //从指定的起点开始BFS
        self.bfs(0, n, distance, pointEdge)
        # 找出距离指定起点的最远的点 ，也就是直径的第一个端点
        diameterFirstPointIndex = self.findMaxDistanceIndex(distance)
        # 从直径的第一个端点再开始BFS
        self.bfs(diameterFirstPointIndex, n, distanceOne, pointEdge)
        # 找出距离第一个端点最远的点 ，也就是直径的第二个端点
        diameterSecondPointIndex = self.findMaxDistanceIndex(distanceOne)
        # 从直径的第二个端点再开始BFS
        self.bfs(diameterSecondPointIndex, n, distanceTwo, pointEdge)

        # 第二直径的值
        secondDiameter = 0

        # 遍历每个点，找到每个点的最远距离更新第二直径

        for i in range(n):
            # 最长的边是第一直径，如果我们把第一直径的两个端点去掉，就可以把第一直径给忽略了
            # 这样只需要在忽略第一直径后剩下的距离找一个最大值就是第二直径

            if i != diameterFirstPointIndex and i != diameterSecondPointIndex:
                # 到i的最远距离的点肯定是第一直径的两个端点之一
                secondDiameter = max(secondDiameter, max(distanceOne[i], distanceTwo[i]))

        return secondDiameter






