"""给你一个整数数组arr和一个整数k 。现需要从数组中恰好移除k个元素，请找出移除后数组中不同整数的最少数目。
示例一
输入：arr = [5, 5, 4], k = 1
输出：1
"""
from typing import List
from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr_counter = Counter(arr)
        arr_num = sorted(arr_counter.values())
        while k>0:
            if k >= arr_num[0]:
                k -= arr_num[0]
                arr_num.pop(0)
            else:
                break
        return len(arr_num)


solu = Solution()
arr = [4,3,1,1,3,3,2]
k = 3

ans = solu.findLeastNumOfUniqueInts(arr, k)
print(ans)
