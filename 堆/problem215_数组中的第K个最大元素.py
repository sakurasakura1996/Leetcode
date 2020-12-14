""""
215. 数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k:int) -> int:
        # 维护小顶堆，然后保持堆中有k个元素
        heap = []
        n = len(nums)
        for i in range(n):
            if len(heap) < k:
                # 直接放入堆中
                heapq.heappush(heap, nums[i])
            elif len(heap) == k:
                if heap[0] < nums[i]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, nums[i])
        return heap[0]


solu = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
ans = solu.findKthLargest(nums, k)
print(ans)


