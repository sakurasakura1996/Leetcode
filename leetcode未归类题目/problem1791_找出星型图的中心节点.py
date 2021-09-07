from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]])->int:
        # 不是这题目也能算中等，记录下每个节点的度不就行了
        degrees = [0] * (len(edges) +1)
        for u, v in edges:
            degrees[u-1] += 1
            degrees[v-1] += 1
        for i, value in enumerate(degrees):
            if value == len(edges):
                return i+1
