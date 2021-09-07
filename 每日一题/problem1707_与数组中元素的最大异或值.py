from typing import List
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        qrs = sorted(enumerate(queries),key=lambda x:x[1][1])
        trie = Trie()
        idx, n = 0, len(nums)
        ans = [0] * len(qrs)
        for i,(x, m) in qrs:
            while idx < n and nums[idx] <= m:
                trie.add(nums[idx])
                idx += 1
            ans[i] = trie.query(x)
        return ans

# 构建一颗前缀树，思想就是用字典，所以有时候也叫字典树
class Trie:
    def __init__(self):
        self.root = {}

    def add(self, x):
        # 向这棵树中加入x节点，以二进制的格式加入
        node = self.root
        for i in range(31, -1, -1):
            bit = x >> i & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def query(self, x):
        # 查询 前缀树中比 x小的节点中和x异或的最大值
        res = 0
        node = self.root
        for i in range(31, -1, -1):
            res <<= 1
            bit = x >> i & 1
            xor = bit ^ 1
            if xor in node:
                res += 1
                node = node[xor]
            elif bit in node:
                node = node[bit]
            else:
                return -1
        return res



# 上次王湘生说到了字典树，确实，很相似，从高位开始不断往下扫描。
# 先构建一颗字典树，往左表示0，往右表示1
# 终于找到了曾经很相似的一道题了， 第421题，数组中两个数的最大异或值。

