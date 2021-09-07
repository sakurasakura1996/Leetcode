"""
347. 前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]
提示：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。
"""
from collections import Counter
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)

        # 这里的字典 根据value进行排序还是需要多多关注一下的。
        # 主要是这里的key参数，它的意思就是，我排序的是一个dict_items属于tuple类型，每个元素中有key和value
        # 那么要根据value排序的话，我们需要指定key为第二个元素也就是key，表达方法就是key= lambda x: x[1]
        cur = sorted(nums_counter.items(), key= lambda x:x[1], reverse=True)
        ans = []
        for idx, value in enumerate(cur):
            if idx < k:
                ans.append(value[0])
        return ans


    def topKFrequent_2(self, nums: List[int], k: int) -> List[int]:
        # python默认最小堆，则将出现的次数取负再入堆。
        # 这里的代码过程是，我先记录所有元素出现的次数，然后将他们全部放入最小堆中，但是出现次数取负。
        # 这样最小堆中的最小的k个元素即为实际最大的k个元素，这时候只需顺序去除堆中前k个元素即可。
        dic = Counter(nums)
        heap, ans = [], []

        for i in dic:
            heapq.heappush(heap,(-dic[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

    # 上面的方法毕竟使用了python自带的排序和数据结构，题解中使用到了堆方法,我们先遍历一遍整个数组，然后哈希表记录
    # 每个数字出现的次数，并形成一个出现次数数组。那就相当于找到出现次数数组中前k大的值，如果给出现次数数组排序的话
    # 较差情况下复杂度不符合要求，所以这里利用小顶堆，然后遍历出现次数数组
    #   1.如果堆得元素个数小于k，就可以直接插入堆中，
    #   2.如果堆得元素个数等于k，则检查堆顶与当前出现次数的大小，如果堆顶更大，则舍弃当前值，否则弹出栈顶元素，并将
    #     当前值插入堆中。
    def topKFrequent_3(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        heap, ans = [], []
        for i in nums_counter:
            if len(heap) < k:
                heapq.heappush(heap, (nums_counter[i], i))
            elif len(heap) == k:
                node = heapq.heappop(heap)
                if node[0] > nums_counter[i]:
                    heapq.heappush(heap, node)
                else:
                    heapq.heappush(heap, (nums_counter[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans


solu = Solution()
nums = [1]
k = 1
ans = solu.topKFrequent_3(nums, k)
print(ans)