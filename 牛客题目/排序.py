"""
题目描述
给定一个数组，请你编写一个函数，返回该数组排序后的形式。
示例1
输入
[5,2,3,1,4]
返回值
[1,2,3,4,5]
示例2
输入
[5,1,6,2,5]
返回值
[1,2,5,5,6]
备注:
数组的长度不大于100000，数组中每个数的绝对值不超过10^9
"""
from typing import List
class Solution:
    def Mysort(self, arr: List[int]):
        # 冒泡排序
        if not arr:
            return
        n = len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def quickSort(self, arr: List[int], left, right):
        # 这里写一下快速排序
        if not arr:
            return
        def partition(array, head, tail):
            pivot = array[head]
            while head < tail:
                while head < tail and array[tail] >= pivot:
                    tail -= 1
                array[head] = array[tail]
                while head < tail and array[head] <= pivot:
                    head += 1
                array[tail] = array[head]
            array[head] = pivot
            return head
        if left < right:
            mid = partition(arr, left, right)
            self.quickSort(arr, left, mid-1)
            self.quickSort(arr, mid+1, right)
        return arr


if __name__ == '__main__':
    solu = Solution()
    arr = [5,1,7,2,5]

    ans = solu.quickSort(arr, 0, len(arr)-1)
    print(ans)