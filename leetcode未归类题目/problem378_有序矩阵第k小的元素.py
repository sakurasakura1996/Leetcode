"""
378. 有序矩阵中第K小的元素
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
示例：
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
返回 13。
提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。
"""
# 最笨的方法，直接遍历一遍，然后题目说了是第k小的元素，而不是第k个不同的元素，所以有重复的元素不需要去掉
# 那我们直接遍历一遍，然后排个序找到第k个值就行了，后续再看看其他简便方法
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans.append(matrix[i][j])
        ans.sort()
        return ans[k-1]

    # 上面的写法总还是比较暴力的，虽然提交之后结果还好，想想更好的思路
    # 题解方法二、归并排序
    # 由题目给出的性质可知，这个矩阵的每一行均为一个有序数组。问题即转化为从这n个有序数组中找第k大的数，可以想到利用归并排序的做法，
    # 归并到第k个数即可停止。一般归并排序是两个数组归并，而本题是n个数组归并，所以需要用小根堆维护，以优化时间复杂度
    # 具体如何归并，可以参考力扣23.合并K个排序链表。
    def kthSmallest_2(self, matrix: List[List[int]], k:int) -> int:
        n = len(matrix)
        import heapq
        pq = [(matrix[i][0], i, 0) for i in range(n)] # 元组中的含义是 数、行数、每行中的第几个数
        heapq.heapify(pq) # heapq.heapify()的用法就是将 list列表转化为堆

        ret = 0
        for i in range(k-1): # 出栈前k个最小的元素
            num, x, y = heapq.heappop(pq)
            if y != n-1:
                heapq.heappush(pq, (matrix[x][y+1], x, y+1))
        return heapq.heappop(pq)[0]

    def kthSmallest_3(self, matrix: List[List[int]], k:int) -> int:
        # 二分查找 矩阵中左上角为最小值，左下角为最大值，我们不断二分查找速度也是比较快的
        n = len(matrix)

        def check(mid):
            # 和mid值进行比较，计算出矩阵中有多少个比mid小的数，返回是否 >= k，这个check计算方法还是比较巧妙的。
            i, j = n-1, 0
            num = 0
            while i>=0 and j<n:
                if matrix[i][j]<=mid:
                    num += i+1
                    j += 1
                else:
                    i -= 1
            return num >= k
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left



solu = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
ans = solu.kthSmallest(matrix, k)
print(ans)

