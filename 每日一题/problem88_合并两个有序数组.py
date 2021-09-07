from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 如果使用额外的空间复杂度，题目会很简单就能思考清楚
        ans = nums1[:m]
        p1 = 0
        p2 = 0
        cur = 0
        while p1 < m and p2 < n:
            if ans[p1] <= nums2[p2]:
                nums1[cur] = ans[p1]
                cur += 1
                p1 += 1
            else:
                nums1[cur] = nums2[p2]
                cur += 1
                p2 += 1
        if p1 < m:
            nums1[cur:] = ans[p1:]
        else:
            nums1[cur:] = nums2[p2:]

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 上面的方法使用了O(m)的空间复杂度，那么能否只使用O(1)的空间复杂度呢，可以，从nums1后面往前开始赋值，就没问题了。
        p1 = m - 1
        p2 = n - 1
        cur = m + n -1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[cur] = nums2[p2]
                p2 -= 1
                cur -= 1
            else:
                nums1[cur] = nums1[p1]
                p1 -= 1
                cur -= 1
        if p2 >= 0:
            nums1[:p2+1] = nums2[:p2+1]
