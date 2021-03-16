"""
剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]
限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
"""
from typing import List
class Solution:
    def getLeastNumbers(self, arr:List[int], k:int) -> List[int]:
        arr.sort()
        return arr[:k]
    # 这个时间复杂度是排序的时间复杂度，最起码得O(nlogn)
    # 那么其实是可以O(N)的复杂度的吧

    def getLeastNumbers(self, arr:List[int], k:int) -> List[int]:
        # 利用一个大根堆实时维护数组的前k个最小值。首先将前k个数插入大根堆中，随后从第k+1个数开始遍历，如果当前遍历到的数比大根堆的堆顶的数要小
        # 就把堆顶的数弹出

