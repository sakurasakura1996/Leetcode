"""
1818. 绝对差值和
给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。

数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。

你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。

在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。
|x| 定义为：
如果 x >= 0 ，值为 x ，或者
如果 x <= 0 ，值为 -x

示例 1：
输入：nums1 = [1,7,5], nums2 = [2,3,5]
输出：3
解释：有两种可能的最优方案：
- 将第二个元素替换为第一个元素：[1,7,5] => [1,1,5] ，或者
- 将第二个元素替换为第三个元素：[1,7,5] => [1,5,5]
两种方案的绝对差值和都是 |1-2| + (|1-3| 或者 |5-3|) + |5-5| = 3

示例 2：
输入：nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
输出：0
解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0

示例 3：
输入：nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
输出：20
解释：将第一个元素替换为第二个元素：[1,10,4,4,2,7] => [10,10,4,4,2,7]
绝对差值和为 |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20

提示：
n == nums1.length
n == nums2.length
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 105
"""
from typing import List
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_copy = nums1.copy()
        nums1_copy.sort()
        MAX_VALUE = 10 ** 9 + 7
        n = len(nums1)
        # 先计算出绝对差值和
        abSubSum = 0
        for i in range(n):
            abSubSum += (abs(nums1[i] - nums2[i])%MAX_VALUE)
            abSubSum %= MAX_VALUE

        def binarySearch(x: int) -> int:
            # 在nums1_copy数组中找到离x最近的元素并返回，nums1_copy已经排好序
            left = 0
            right = n-1
            while left <= right:
                mid = left + (right - left) // 2
                if nums1_copy[mid] == x:
                    return x
                elif nums1_copy[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            if left > n-1:
                return nums1_copy[right]
            elif right < 0:
                return nums1_copy[left]
            elif abs(nums1_copy[left] - x) <= abs(nums1_copy[right] - x):
                return nums1_copy[left]
            else:
                return nums1_copy[right]

        ans = 0
        for i in range(n):
            abSum = abs(nums1[i] - nums2[i])
            # 然后在nums1_copy数组中用二分查找找到和nums2[i]差值绝对值最小的元素。然后再不断比较 abSum 和 这个元素与nums2[i]差值绝对值的差值
            # 找出其中最大的就可以了，因为差值最大，说明总的绝对差值和是降低最少的
            x = binarySearch(nums2[i])
            ans = max(ans, abSum - abs(x - nums2[i]))
        return abSubSum - ans


if __name__ == '__main__':
    solu = Solution()
    nums1 = [1,10,4,4,2,7]
    nums2 = [9,3,5,1,7,4]
    ans = solu.minAbsoluteSumDiff(nums1, nums2)
    print(ans)
