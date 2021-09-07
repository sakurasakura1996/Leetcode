from typing import List
from collections import Counter
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # 首先，肯定要有前缀和对吧，先行计算好，然后可以减少循环过程中的复杂度。
        m = len(matrix)
        n = len(matrix[0])
        matSum = [[0] * (n+1) for _ in range(m+1)]
        matSum[1][1] = matrix[0][0]
        for i in range(1, m+1):
            matSum[i][1] = matSum[i-1][1] + matrix[i-1][0]
        for i in range(1, n+1):
            matSum[1][i] = matSum[1][i-1] + matrix[0][i-1]
        for i in range(2, m+1):
            for j in range(2, n+1):
                matSum[i][j] = matSum[i][j-1] + matSum[i-1][j] - matSum[i-1][j-1] + matrix[i-1][j-1]
        ans = 0
        # 接下来如果要暴力法遍历的话，其实不好说能不能过啊，先试试, 结果是超时了。
        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(i, m+1):
                    for l in range(j, n+1):
                        mat_sum = matSum[k][l] - matSum[k][j-1] - matSum[i-1][l] + matSum[i-1][j-1]
                        if mat_sum == target:
                            ans += 1
        return ans

    def numSubmatrixSumTarget2(self, matrix: List[List[int]], target: int) -> int:
        def subarraySum(nums: List[int], k: int) -> int:
            mp = Counter([0])  # 这里加0应该能理解了吧
            count = pre = 0
            for x in nums:
                pre += x
                if pre - k in mp:
                    count += mp[pre - k]
                mp[pre] += 1
            return count

        m, n = len(matrix), len(matrix[0])
        ans = 0
        # 枚举上边界, 因为相比560，这道题是二维的了，我们如果不想暴力，还是得先计算好一维，然后将二维转化为一维。
        for i in range(m):
            total = [0] * n  #　每一列上值的和
            # 枚举下边界
            for j in range(i, m):
                for c in range(n):
                    # 更新每列的元素和
                    total[c] += matrix[j][c]
                # 我感觉其实也就是下面的代码和这里的 for c in range变成了串行的而不是嵌套的，所以节省了时间复杂度啊。
                ans += subarraySum(total, target)


        return ans


if __name__ == '__main__':
    solu = Solution()
    matrix = [[1,-1],[-1,1]]
    target = 0
    ans = solu.numSubmatrixSumTarget(matrix, target)
    print(ans)


