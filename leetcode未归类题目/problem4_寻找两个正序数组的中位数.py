from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)
        if m == 0 and n == 0:
            return
        if m == 0:
            if n % 2 == 1:
                return float(nums2[n//2])
            else:
                return float(nums2[n//2]+nums2[n//2-1])/2

        if n == 0:
            if m % 2 == 1:
                return float(nums1[m//2])
            else:
                return float(nums1[m//2]+nums1[m//2-1])/2

        p1 = p2 = 0
        ans = []
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                ans.append(nums1[p1])
                p1 += 1
            else:
                ans.append(nums2[p2])
                p2 += 1
        if p1 < m:
            ans.extend(nums1[p1:])
        else:
            ans.extend(nums2[p2:])
        if len(ans) % 2 == 1:
            return float(ans[len(ans) // 2])
        else:
            return float(ans[len(ans)//2-1] + ans[len(ans)//2])/2


if __name__ == '__main__':
    solu = Solution()
    nums1 = [0,0]
    nums2 = [0,0]
    ans = solu.findMedianSortedArrays(nums1, nums2)
    print(ans)
