import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        # 要维护一个大顶堆，如果后面的数大于堆顶，则换掉
        n = len(tinput)
        if k > n:
            return []
        heap = [-x for x in tinput[:k]]
        heapq.heapify(heap)
        for num in tinput[k:]:
            if -num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -num)
        ans = []
        while heap:
            ans.append(-heapq.heappop(heap))
        return ans[::-1]


if __name__ == '__main__':
    solu = Solution()
    nums = [4,5,1,6,2,7,3,8]
    k = 0
    ans = solu.GetLeastNumbers_Solution(nums, k)
    print(ans)