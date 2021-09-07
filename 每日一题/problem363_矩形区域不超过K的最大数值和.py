from typing import List
from copy import deepcopy
from sortedcontainers import SortedList
import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # 困难题，暴力法我们也写下熟悉熟悉题目。肯定的，这样写，肯定通过不了
        m = len(matrix)
        n = len(matrix[0])
        # 先对数据进行一些处理，计算出每个节点到原点的矩形范围内数值的和
        origin_sum = deepcopy(matrix)
        # 边界初始化
        for i in range(1, m):
            origin_sum[i][0] += origin_sum[i-1][0]
        for i in range(1, n):
            origin_sum[0][i] += origin_sum[0][i-1]

        for i in range(1, m):
            for j in range(1, n):
                origin_sum[i][j] += (origin_sum[i-1][j] + origin_sum[i][j-1] - origin_sum[i-1][j-1])

        print(origin_sum)
        ans = -float('inf')
        for i in range(m):
            for j in range(n):
                if matrix[i][j] <= k and abs(k - matrix[i][j]) < abs(k - ans):
                    ans = matrix[i][j]
                if origin_sum[i][j] <= k and abs(k - origin_sum[i][j]) < abs(k - ans):
                    ans = origin_sum[i][j]
                for p in range(i):
                    for q in range(j):
                        if p == 0 and q == 0 and origin_sum[i][j] <= k and abs(k - origin_sum[i][j])<abs(k-ans):
                            ans = k - origin_sum[i][j]
                        elif p == 0 and q > 0:
                            tmp_sum = origin_sum[i][j] - origin_sum[i][q-1]
                            if tmp_sum <= k and abs(k-tmp_sum) < abs(k-ans):
                                ans = tmp_sum
                        elif p > 0 and q == 0:
                            tmp_sum = origin_sum[i][j] - origin_sum[p-1][j]
                            if tmp_sum <= k and abs(k - tmp_sum) < abs(k - ans):
                                ans = tmp_sum
                        elif p > 0 and q > 0:
                            tmp_sum = origin_sum[i][j] - origin_sum[i][q-1] - origin_sum[p-1][j] + origin_sum[p-1][q-1]
                            if tmp_sum <= k and abs(k - tmp_sum) < abs(k - ans):
                                ans = tmp_sum
        return ans

    def maxSumSubmatrix2(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        res = float('-inf')
        # 左边界
        for left in range(col):
            # 初始化nums（这个nums就是我们后面要用来求接近K的）
            nums = [0] * row
            # 右边界
            for right in range(left, col):
                for i in range(row):
                    nums[i] += matrix[i][right]
                # 在left, right为边界下的矩阵(在这里已经降维成1维的nums了)，
                # 下面这段求不超过k的最大数值和（跟前面我们讲的如出一辙）
                # 用来存cum的array（已排序）
                array = [0]
                cum = 0
                for num in nums:
                    cum += num
                    loc = bisect.bisect_left(array, cum - k)
                    if loc < len(array):
                        res = max(res, cum - array[loc])
                    bisect.insort(array, cum)
        return res

    def maxSumSubmatrix3(self, matrix: List[List[int]], k: int) -> int:
        ans = float("-inf")
        m, n = len(matrix), len(matrix[0])

        for i in range(m):  # 枚举上边界
            total = [0] * n
            for j in range(i, m):  # 枚举下边界
                for c in range(n):
                    total[c] += matrix[j][c]  # 更新每列的元素和

                totalSet = SortedList([0])
                s = 0
                for v in total:
                    s += v
                    lb = totalSet.bisect_left(s - k)
                    if lb != len(totalSet):
                        ans = max(ans, s - totalSet[lb])
                    totalSet.add(s)

        return ans

if __name__ == '__main__':
    solu = Solution()
    matrix = [[2,2,-1]]
    k = 0
    ans = solu.maxSumSubmatrix(matrix, k)
    print(ans)



