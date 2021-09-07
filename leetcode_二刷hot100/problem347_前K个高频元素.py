from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        # print(nums_counter)
        # print(type(nums_counter))
        nums_counter = sorted(nums_counter.items(), key=lambda x:x[1],reverse=True) # sorted返回的东西是list
        print(nums_counter)
        print(dict(nums_counter))  # 还可以直接将用dict再把这个list变回dict啊
        num = 0
        ans = []
        # print(type(nums_counter))
        for key in nums_counter:
            if num < k:
                ans.append(key[0])
                num += 1
            else:break
        return ans

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        # 上面的实现，我们可以直接调用内置函数
        nums_counter = Counter(nums)
        counter = nums_counter.most_common(k)
        print(counter)
        return [x[0] for x in counter]
        # ans = []
        # num = 0
        # for key in counter:
        #     if num < k:
        #         ans.append(key[0])
        #         num += 1
        #     else:
        #         break
        # return ans

    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        # 上面的方法,算法复杂度位O(NlogN)，题目要求是优于O(NlogN),在这里，我们可以利用堆的思想，建立一个小顶堆，便后遍历 出现次数数组
        # 分析时间复杂度，先遍历一遍数组记录出现次数，时间复杂度为O(N),然后遍历出现次数数组，由于堆的大小至多为k，每次操作堆需要O（logk）
# 所以时间复杂度有原来的排序O(NlogN)变成了O(NlogK)了。
        nums_counter = Counter(nums)
        heap = []
        for key, value in nums_counter.items():
            if len(heap) >= k:
                if value > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))
            else:
                heapq.heappush(heap, (value, key))
        return [item[1] for item in heap]

if __name__ == '__main__':
    solu = Solution()
    nums = [4,1,-1,2,-1,2,3]
    k = 2
    ans = solu.topKFrequent3(nums, k)
    print(ans)