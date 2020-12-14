"""
703. 数据流中的第K大元素
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。
你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，
返回当前数据流中第K大的元素。
示例:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明:
你可以假设 nums 的长度 ≥ k-1 且 k ≥ 1。
"""
from typing import List
import heapq
# 啊，我好笨啊，如果一直往堆中加入数据的话，那第k大的数又怎么能找到呢
# 所以这道题正确使用堆的方法就是，维持堆中只有k个数，如果加入的数据比堆顶的数还要小直接就忽略操作啊。


class KthLargest:
    # 注意这里的方法超时了，原因是，我并未保持大顶堆的数量，只要add就往里面添加数据，然后再取出前k大的数，到后面肯定会很超时。
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        # 运用heapq堆模块会对列表进行排序吗，那堆中第K大的元素是不是直接用索引来提取出来呢?然而并不是
        # 那么如何取出第k大的数呢？解法见上方解析,或者 heapq.nlargest(n, heap)
        heapq.heappush(self.heap, val)
        num = heapq.nlargest(self.k, self.heap)[self.k-1]
        return num


class Solution:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        # 使用小顶堆哦，然后维持堆中只有k个数，那么最小的数即为所求
        for num in nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, num)
            elif len(self.heap) == self.k and heapq.nsmallest(1, self.heap)[0] < num:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return heapq.nsmallest(1, self.heap)[0]
        elif len(self.heap) == self.k and heapq.nsmallest(1, self.heap)[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
            return heapq.nsmallest(1, self.heap)[0]
        else:
            return heapq.nsmallest(1, self.heap)[0]


k = 3
arr = [4, 5, 8, 2]
obj = Solution(k, arr)
# print(obj.heap)
ans = []
ans.append(obj.add(3))
ans.append(obj.add(5))
ans.append(obj.add(10))
ans.append(obj.add(9))
ans.append(obj.add(4))
print(ans)





