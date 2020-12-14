""""
1046. 最后一块石头的重量
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
示例：
输入：[2,7,4,1,8,1]
输出：1
解释：
先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
提示：
1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
# 平常做堆的题目比较少，这道题做之前已经知道可以用堆来写了，所以我们要思考其中运用堆的原因。
# 最大的两块石头->这个立意是可以发现堆的数据结构能很好的解决问题
from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 注意哦，这里要的是大顶堆哦，python默认是小顶堆，大顶堆就把数据取负
        heap = []
        n = len(stones)
        for i in range(n):
            heapq.heappush(heap, -stones[i])
        while len(heap) > 1:
            heap_len = len(heap)
            max1 = heapq.heappop(heap)
            max2 = heapq.heappop(heap)
            if max1 != max2:
                heapq.heappush(heap, -abs(max1 - max2))  # 当然只要存入堆中的数据都要取负
            elif heap_len == 2:
                return 0
        return abs(heapq.heappop(heap))


solu = Solution()
stones = [3, 7, 2]
ans = solu.lastStoneWeight(stones)
print(ans)
