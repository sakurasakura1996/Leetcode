from typing import List
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # 先计算前缀和
        preSum = [0]
        n = len(candiesCount)
        for i in range(n):
            preSum.append(preSum[-1]+candiesCount[i])
        m = len(queries)
        answer = [False] * m
        for i in range(m):
            type, day, cap = queries[i]
            print(preSum[type])
            print((day+1)*cap)
            if preSum[type] < (day+1) or preSum[type-1] >= (day+1) * cap:
                answer[i] = False
            else:
                answer[i] = True
        return answer


if __name__ == '__main__':
    solu = Solution()
    candiesCount = [7,4,5,3,8]
    queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
    ans = solu.canEat(candiesCount, queries)
    print(ans)