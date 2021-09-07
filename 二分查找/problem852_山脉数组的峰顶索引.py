from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(1, n-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                return i

    def peakIndexInMountainArray2(self, arr: List[int]) -> int:
        # 二分法
        n = len(arr)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] <= arr[mid] <= arr[mid+1]:
                left = mid + 1
            elif arr[mid-1] >= arr[mid] >= arr[mid+1]:
                right = mid - 1


if __name__ == '__main__':
    solu = Solution()
    arr = [3,4,5,1]
    ans = solu.peakIndexInMountainArray2(arr)
    print(ans)