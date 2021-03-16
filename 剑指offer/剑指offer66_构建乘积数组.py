"""
剑指 Offer 66. 构建乘积数组
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
提示：
所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
"""
# 这道题我考研之后面试公司的笔试题做过，当时没想出来，其实应该是两遍遍历，从左往右乘一遍，从右往左乘一遍
from typing import List
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if not a:
            return a
        a_len = len(a)
        ans = [1] * a_len
        for i in range(1, a_len):
            ans[i] = ans[i-1] * a[i-1]

        cur = a[-1]
        for i in range(a_len-2, -1, -1):
            ans[i] = ans[i] * cur
            cur = cur * a[i]
        return ans

solu = Solution()
a = [1, 2, 3, 4, 5]
ans = solu.constructArr(a)
print(ans)
