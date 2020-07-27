"""
5465. 子树中标签相同的节点数  显示英文描述
通过的用户数 14
尝试过的用户数 15
用户总通过次数 14
用户总提交次数 16
题目难度 Medium
给你一棵树（即，一个连通的无环无向图），这棵树由编号从 0  到 n - 1 的 n 个节点组成，且恰好有 n - 1 条 edges 。
树的根节点为节点 0 ，树上的每一个节点都有一个标签，也就是字符串 labels 中的一个小写字符（编号为 i 的 节点的标签就是 labels[i] ）
边数组 edges 以 edges[i] = [ai, bi] 的形式给出，该格式表示节点 ai 和 bi 之间存在一条边。
返回一个大小为 n 的数组，其中 ans[i] 表示第 i 个节点的子树中与节点 i 标签相同的节点数。
树 T 中的子树是由 T 中的某个节点及其所有后代节点组成的树。
"""
from typing import List
from functools import lru_cache

# class Solution:
#     def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
#         # 这个方法有一个地方没能解决，那就是 edges中的边，不一定是按照父节点到子节点的顺序写入的，比如[1,2]并不是说2肯定是1的子节点啊。
#         @lru_cache(None)
#         def solve(i:int,label:str)->int:
#             # 根z据该节点的id，返回其子树中相同标签的个数
#             if labels[i] == label:
#                 ans = 1
#             else:
#                 ans = 0
#             for edge in edges:
#                 if i == edge[0]:
#                     node = edge[1]
#                     ans += solve(node, label)
#             return ans
#
#         ans_list = []
#         for i in range(n):
#             ans_list.append(solve(i,labels[i]))
#         return ans_list

from collections import defaultdict, Counter
# 下面这个代码写的看着有点吃力，最后面的代码写的比较好理解
# class Solution:
#     def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
#
#         class TreeNode:   # 妈的本来也想着是不是要先还原出这颗树啊
#             def __init__(self, idx):
#                 self.val = idx
#                 self.children = []
#
#         visited = {0}
#         join = defaultdict(list)
#         for x, y in edges:   # 我上面提到的问题所在，这里是正反都记录了一次
#             join[x].append(y)
#             join[y].append(x)
#
#         root = TreeNode(0)
#
#         def add(root):
#             for child in join[root.val]:
#                 if child not in visited:
#                     root.children.append(TreeNode(child))
#                     visited.add(child)
#             for child in root.children:
#                 add(child)
#
#         add(root)
#
#         ans = [0] * n
#
#         def helper(root):
#             if not root:
#                 return [0] * 26
#             res = [0] * 26
#             for child in root.children:
#                 for idx, cnt in enumerate(helper(child)):
#                     res[idx] += cnt
#             idx = ord(labels[root.val]) - 97
#             res[idx] += 1
#             ans[root.val] = res[idx]
#             return res
#
#         helper(root)
#         return ans

# 看看别人的代码是怎么写的
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        e = defaultdict(list)
        for x in edges:
            e[x[0]].append(x[1])
            e[x[1]].append(x[0])
        visit = [False] * n
        ret = [0] * n

        def work(h):
            visit[h] = True

            s = Counter()
            s[labels[h]] = 1
            for x in e[h]:
                if not visit[x]:
                    tmp = work(x)
                    for y in tmp:
                        s[y] += tmp[y]
            ret[h] = s[labels[h]]
            return s

        work(0)
        return ret


solu = Solution()
n = 4
edges = [[0,2],[0,3],[1,2]]
labels = "aeed"

ans = solu.countSubTrees(n, edges, labels)

print(ans)