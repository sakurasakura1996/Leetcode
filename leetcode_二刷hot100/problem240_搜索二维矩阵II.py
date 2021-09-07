# 二维矩阵从上到下，从左到右都是升序，编写最好的时间复杂度来找到目标值target
# 简单的话，直接暴力查找，平方复杂度，用二分查找的话会快一些，但是这个二维如何用二分法呢，是逐行遍历，然后每一行内部用二分法吗
# 还是选择某一行的时候就用二分法，然后这一行内部还是用二分法呢，如果可以实现的话，肯定是后面的思路更快啊。
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 思路比较简单点的，对时间复杂度要求不是特别高的话，我们就只在每一行上进行二分搜索算了
        def binary_search(nums, target):
            length = len(nums)
            left = 0
            right = length - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid-1
            return False

        for line in matrix:
            if line[0] <= target and line[-1] >= target and binary_search(line, target):
                return True
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        # 因为每行每列都是已经排好序的，那么，我们可以以对角线来进行迭代啊，只不过迭代到某一步的时候要对行和列分别进行二分查找
        # 这个思路我之前应该看到过，左上角和右下角不好直接二分，但是右上角和左下角都是简单的，因为两个方向一个增一个减
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = col - 1
        while matrix[i][j] != target:
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
            if i >= row or j < 0:
                return False
        return True


if __name__ == '__main__':
    solu = Solution()
    matrix = [[-5]]
    target = -5
    ans = solu.searchMatrix(matrix, target)
    print(ans)