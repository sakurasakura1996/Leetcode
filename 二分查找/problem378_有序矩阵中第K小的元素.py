from typing import List
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 暴力法
        n = len(matrix)
        # 题解中看到了一个python的骚操作我竟然还没看到过，
        ans = sorted(sum(matrix, []))    # 为什么 sum(matrix, [])能将二维数组伸展成一维的呢。。。
        return ans[k-1]

    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        # 每一行均为一个有序数组，问题转化为这n个有序数组中找第k大的数，可以想到利用归并排序的做法。一般归并排序是两个数组的归并，这里是n个，所以需要
        # 用小根堆来维护。
        n = len(matrix)
        heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(heap)

        for i in range(k-1):
            num, x, y = heapq.heappop(heap)
            if y != n - 1:
                heapq.heappush(heap, (matrix[x][y+1], x, y+1))
        return heapq.heappop(heap)[0]

    def kthSmallest3(self, matrix: List[List[int]], k: int) -> int:
        # 二分查找
        n = len(matrix)

        def count(mid):
            i, j = n-1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i+1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[n-1][n-1]
        while left < right:
            mid = left + (right - left) // 2
            if count(mid):
                right = mid
            else:
                left = mid + 1
        return left




if __name__ == '__main__':
    solu = Solution()
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    ans = solu.kthSmallest2(matrix, k)
    print(ans)
