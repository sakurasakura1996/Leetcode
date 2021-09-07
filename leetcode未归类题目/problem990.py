"""
990.等式方程的可满足性
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。
在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 
示例 1：
输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
"""
# 因为题目要求了每个字符串方程都是四个字符组成的，左右单字母变量，中间是 == 后者 != 这两种
# false的情况就是只要存在a==b 那么就不能又a!=b或者b!=a同理 出现了a!=b 则不能有a==b or b==a
# 这一类的连接问题是典型的并查集方法来做。
from typing import List


class UF:
    parent = {}

    def __init__(self, equations):
        for eq in equations:
            self.parent[eq[0]] = eq[0]
            self.parent[eq[3]] = eq[3]

    def find(self,x):
        # 找到x的根节点
        while x!=self.parent[x]:
            x = self.parent[x]
        return x

    def connected(self,p,q):
        # 判断两个节点是否在同一个联通分量中
        return self.find(p) == self.find(q)

    def union(self,p,q):
        # 将p，q两个进行合并操作,先用connected来判断两个是否在同一个连通分量里
        if self.connected(p,q):
            return
        self.parent[self.find(p)] = self.find(q)  # 这里的合并操作是，如果他们两目前不属于同一个连通分量，那么把q的根节点作为
        # p的根节点的父节点，这样原来的两个连通分量就结合成一个了

# 这里没有做路径压缩，这直接导致find union connected 的时间复杂度最差的情况退化到O(N)
# 当然优化也不难，我们只需要给每一个顶层元素设置一个size用来表示连通分量的大小，这样union的时候我们将小的拼接到大的上即可。
# 另外find的时候我们甚至可以路径压缩，将树高限定到常数，这样时间复杂度可以降低到O(1)。



class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(equations)
        for eq in equations:
            if eq[1] == '=':
                uf.union(eq[0], eq[3])
        for eq in equations:
            if eq[1] == '!' and uf.connected(eq[0],eq[3]):
                return False
        return True



solu = Solution()
equations = ["a==b","b!=a"]
ans = solu.equationsPossible(equations)
print(ans)

