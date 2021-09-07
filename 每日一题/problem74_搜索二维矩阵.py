from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        nums = []
        for line in matrix:
            nums.extend(line)

        left = 0
        right = m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        # 先二分查找列，找到最后一个不大于目标值的元素，然后搜索这一行。
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])

        up = 0
        down = m - 1
        while up <= down:
            mid = up + (down - up) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                up = mid + 1
            else:
                down = mid - 1
        nums = matrix[down]
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == '__main__':
    solu = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    ans = solu.searchMatrix2(matrix, target)
    print(ans)