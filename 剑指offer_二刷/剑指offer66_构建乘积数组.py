"""
剑指 Offer 66. 构建乘积数组
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积,
即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
提示：
所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
"""
from typing import List
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if not a:
            return a
        n = len(a)
        ans = a.copy()
        cur = 1
        for i in range(n):
            ans[i] = cur
            cur *= a[i]
        cur = 1
        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * cur
            cur *= a[i]
        return ans


if __name__ == '__main__':
    solu = Solution()
    a = [1, 2, 3, 4,5]
    ans = solu.constructArr(a)
    print(ans)


