class DSU(object):
    def __init__(self, N):
        self.p = [x for x in range(N)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution(object):
    def __init__(self):
        self.answer = {}

    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        if threshold >= n:
            return [False] * len(queries)
        res = []
        dsu = DSU(n + 1)

        for i in range(threshold + 1, n + 1):
            times = 2
            while i * times <= n:
                dsu.union(i, i * times)
                times += 1

        for x, y in queries:
            if dsu.find(x) == dsu.find(y):
                res += [True]
            else:
                res += [False]
        return res

