"""
剑指 Offer 51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:
输入: [7,5,6,4]
输出: 5
限制：
0 <= 数组长度 <= 50000
"""
# 从problem315.计算右侧小于当前元素的个数 这道题来的，提示使用归并排序来求逆序对的总数。
# 这道题暴力解法应该是肯定会超时的。
from typing import List
class Solution:
    def reversePairs(self, nums: List[int])->int:

        if not nums or len(nums) < 2:
            return 0
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n-1)

    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) //2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid+1, r)
        i, j, pos = l, mid+1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
                # 这里的思考很耐人寻味，因为这里有两种写法。
                # 1.这里题解中的写法是第一种思考方式，就是第一个子区间（左边）归并回去的时候，A[i] <= B[j],我们的思考就是B[j]前面的肯定小于
                #    A[i]啊，不然A[i]已经归并进去了。所以这个时候ans应该加上 (j-(mid+1))
                # 2.第二种思考方式就是第二个子区间（右边）归并进数组的时候，A[i] >= B[j]，这个时候，A[i]及其后面的都是满足条件的
                #   所以ans应该加上 (mid-i+1)
            else:
                tmp[pos] = nums[j]
                j += 1
                # inv_count += (mid - i + 1)
            pos += 1

        while i <= mid:
            # 尤其这里要注意啊，如果是第一种思考方式的话，并且左边的子区间还没有遍历完，那么每遍历一个都还要加上右边区间的长度啊。
            tmp[pos] = nums[i]
            inv_count += (j - (mid + 1))
            i += 1
            pos += 1
        while j <= r:
            # 同理注意这里如果采用的是第二种思考方式，并且右边的子区间还没有遍历完,那么就不用遍历了啊，因为右边的值都大于左区间的值，不用加了
            tmp[pos] = nums[j]
            j += 1
            pos += 1

        nums[l:r+1] = tmp[l:r+1]
        return inv_count







