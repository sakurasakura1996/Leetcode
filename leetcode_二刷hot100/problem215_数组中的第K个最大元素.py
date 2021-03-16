from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # 这道题应该不是让我们写出上面的代码，那我们要不用一下堆看看，建立一个大根堆，做k-1次删除操作后堆顶元素就是我们要找的答案。
        ans = heapq.nlargest(k, nums)[k-1]
        return ans

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        # 当然也不是想让我们直接调用现成的容器, heapq默认创建的是最小堆
        if k == 0:
            return None
        heap = [x for x in nums[:k]]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0]

