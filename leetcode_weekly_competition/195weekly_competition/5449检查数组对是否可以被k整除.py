
"""
给你一个整数数组 arr 和一个整数 k ，其中数组长度是偶数，值为 n 。

现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。

如果存在这样的分法，请返回 True ；否则，返回 False 。



示例 1：

输入：arr = [1,2,3,4,5,10,6,7,8,9], k = 5
输出：true
解释：划分后的数字对为 (1,9),(2,8),(3,7),(4,6) 以及 (5,10)
"""
from typing import List
class Solution:
    def canArrange_1(self, arr: List[int], k: int) -> bool:
        if not arr:
            return True
        n = len(arr)
        x = arr[0]
        for i in range(1,n):
            y = arr[i]
            if (x + y)%k == 0:
                arr.remove(x)
                arr.remove(y)
                return self.canArrange(arr, k)
        return False
    # 上面的解法超时了。
    # 这题没做出来，可以将它作为一个很好的示例程序，这一类成对的整除问题，可以先把他们除以那个数，然后取余数就可以了
    # 那么数组arr中的数都变成了[0,k)之间的数。这时候我们考虑如果数组中0的个数不是偶数的话，那么就为False，如果0
    # 的个数为偶数的话，那么再看看剩下的数字，排序之后，就首尾两个数字进行相加，如果为k则肯定满足条件了。
    def canArrange_2(self, arr: List[int], k:int) -> bool:
        for idx, num in enumerate(arr):
            arr[idx] %= k
        arr.sort()
        zero_num = 0
        arr_len = len(arr)
        for i in range(arr_len):
            if arr[i] == 0:
                zero_num += 1
        if zero_num % 2 != 0:
            return False
        left = zero_num
        right = arr_len-1
        while left < right:
            if arr[left] + arr[right] != k:
                return False
            left += 1
            right -= 1
        return True
    # 这道题可以作为一个很好的例题，可能之前没怎么碰到过，以后请记住这类题的解法哦




solu = Solution()
arr = [-1,1,-2,2,-3,3,-4,4]
k = 3
ans = solu.canArrange(arr,k)
print(ans)
