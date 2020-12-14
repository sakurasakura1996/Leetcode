"""
332. 重新安排行程
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。
所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。
说明:
如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
示例 1:
输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]

示例 2:
输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
"""
from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:return []
        n = len(tickets)
        tickets_dic = defaultdict(list)
        for ticket in tickets:
            tickets_dic[ticket[0]].append(ticket[1])
        # 要想字符排序可以设置邻接表排序
        for f in tickets_dic:
            tickets_dic[f].sort()
        ans = []
        def dfs(f):
            # 下面的深搜回溯对我来说实在难以思考清楚啊，确实这种表述是对的且代码很简洁。
            # 我当时考虑这段代码的问题会不会出现在，比如 A->B, A->C，那么A->B是排在前面的，但是如果B接下来没有什么路径了，岂不是不行
            # 注意看代码，如果不行，这个时候就把B插入了ans数组中，为什么，因为所有的路径都要遍历一遍，如果B接下来不能遍历其他的地方，
            # 那不恰好是说明B就是终点站了吗，所以这样表述很牛逼。
            while tickets_dic[f]:
                dfs(tickets_dic[f].pop(0))
            ans.insert(0, f)
        dfs("JFK")
        return ans

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 标准的回溯，下面的代码更好读懂理解
        graph = defaultdict(list)
        city_link = defaultdict(int)
        for x, y in tickets:
            graph[x].append(y)
            city_link[(x,y)] += 1

        ans = ["JFK"]
        # returned result should have tickets + 1 cities
        def dfs(cur):
            if len(ans) == len(tickets) + 1:
                return True

            for dest in sorted(graph[cur]):
                if city_link[(cur, dest)] != 0:
                    # 尝试这个行不行
                    city_link[(cur, dest)] -= 1
                    ans.append(dest)
                    if dfs(dest):
                        return True

                    # 撤销
                    ans.pop()
                    city_link[(cur, dest)] += 1
            return False

        dfs("JFK")
        return ans


