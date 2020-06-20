"""
721.账户合并
给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails
表示该帐户的邮箱地址。现在，我们想合并这些帐户。如果两个帐户都有一些共同的邮件地址，则两个帐户必定属于同一个人。请注意，即使两个帐户具有相同的名称，
它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的帐户，但其所有帐户都具有相同的名称。
合并帐户后，按以下格式返回帐户：每个帐户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。accounts 本身可以以任意顺序返回。
"""
# from typing import List
# class UF:
#     parent = {}
#     def __init__(self, accounts:List[List[str]]):
#         # 并查集方法中init每次做的就是每个节点都是单独的一个连通分量
#         # 因为存在同名的问题，我们的parent哈希表key就存储索引吧
#         for i in range(len(accounts)):
#             flag = 1
#             for j in range(1,len(accounts[i])):
#                 if accounts[i][j] in self.parent:
#                     for p in range(1,len(accounts[i])):
#                         self.parent[accounts[i][p]] = self.parent[accounts[i][j]]
#                     flag = 0
#                     break
#             if flag:
#                 for j in range(1,len(accounts[i])):
#                     self.parent[accounts[i][j]] = i
#
#     def find(self,x):
#         while x!= self.parent[x]:
#             x = self.parent[x]
#         return x
#
#     def union(self,p,q):
#         if self.connected(p,q):return
#         self.parent[]



# 怎么说呢，这道题我自己敲不出来，总感觉思路是有，但是编码很难上手。是敲代码自己敲的太少了吗
# 而且，不要动不动就看答案行不行，不然这样一点效果都没有。
import collections
class DSU:
    def __init__(self):
        self.p = list(range(10001))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution(object):
    def accountsMerge(self, accounts):
        dsu = DSU()
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])

        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)

        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]


