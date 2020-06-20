"""
547.朋友圈
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。
所谓的朋友圈，是指所有朋友的集合。
给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。
你必须输出所有学生中的已知的朋友圈总数。
示例 1:
输入:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。
示例 2:
输入:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出: 1
说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
注意：
N 在[1,200]的范围内。
对于所有学生，有M[i][i] = 1。
如果有M[i][j] = 1，则有M[j][i] = 1。
"""
# 并查集类的题目通常都有一个很明显的题目特点：那就是传递性，a和b有这种关系，b和c有这种关系，那么a和c也有这种关系，这类题目很大概率可以用
# 并查集的思想方法来做，总的来说就是用集合来表达题目中的意思。
# 最开始，所有的学生都各自是一个朋友圈，然后这个时候开始合并，如果a和b是一个朋友圈，就把a的根节点指向b的根节点。最后还有几个集合就是朋友圈的个数

from typing import List

class UF:
    def __init__(self, M: List[List[int]]):
        self.parent = [i for i in range(len(M))]   # parent[i]表示第i个同学的父节点是第parent[i]个同学
        # for i in range(len(M)):
        #     for j in range(i, len(M[0])):
        #         if M[i][j] == 1:
        #             self.parent[j] = self.find(i)

    def find(self,x):
        # 查找第x个同学的根节点，
        while x!=self.parent[x]:
            x = self.parent[x]
        return x

    def connected(self,p,q):
        return self.find(p) == self.find(q)


    def union(self,p,q):
        if self.connected(p,q):return
        self.parent[self.find(p)] = self.find(q)


    def ans(self):
        ans = set()
        for i in range(len(self.parent)):
            ans.add(self.find(i))
        return len(ans)


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or len(M) == 1:
            return len(M)
        uf = UF(M)

        for i in range(len(M)):
            for j in range(i, len(M[0])):
                if M[i][j] == 1:
                    uf.union(i,j)
        ans = uf.ans()
        return ans

# 除了并查集方法，还可以用BFS和DFS来解决以上问题。

solu = Solution()
# M = [[1,1,1],
#      [1,1,0],
#      [1,0,1]]
# M = [[1,0,0,1],
#      [0,1,1,0],
#      [0,1,1,1],
#      [1,0,1,1]]
M = [[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
     [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
     [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
     [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
     [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
     [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
     [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
ans = solu.findCircleNum(M)
print(ans)


