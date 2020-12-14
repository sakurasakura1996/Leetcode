"""
5477. 排布二进制网格的最少交换次数
给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。
一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。
请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。
主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。
示例 1：
输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
输出：3
示例 2：
输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
输出：-1
解释：所有行都是一样的，交换相邻行无法使网格符合要求。
示例 3：
输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
输出：0
提示：
n == grid.length
n == grid[i].length
1 <= n <= 200
grid[i][j] 要么是 0 要么是 1 。
"""
# 这道题是真的搞不太定，看题解中，主要有贪心算法和冒泡排序，有点被惊到了哈哈哈，我擦，还有冒泡排序
from typing import List
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # 贪心算法，统计每一行从右向左连续0的个数
        if not grid:
            return 0
        # 统计每一行，从右向左连续0的个数
        n = len(grid)
        zero_nums = []
        for i in range(n):
            j = n - 1
            while j >= 0 and grid[i][j] == 0:
                j -= 1
            zero_nums.append(n - 1 - j)
        # 贪心算法，从上到下查找满足条件的最小下标，即为交换到当前行的次数
        cnt = 0
        for i in range(n-1):
            need_zeros = n - 1 - i

            j = i
            while j < len(zero_nums) and zero_nums[j] < need_zeros:
                j += 1
            # 没找到则说明不满足条件
            if j == len(zero_nums):
                return -1
            # 增加交换次数
            cnt += j - i
            # 交换数值
            while j > i:
                zero_nums[j], zero_nums[j-1] = zero_nums[j-1], zero_nums[j]
                j -= 1
        return cnt

    def minSwaps_2(self, grid: List[List[int]]) -> int:
        # 冒泡思路
        # 思路其实很简单，找到grid中的每行在满足要求的二进制网格中的位置序号，并将其保存到一个数组中
        # 然后对这个数组进行冒泡排序，记录其前后位置互换的次数，这个交换次数就是题目要求的最小的交换次数
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        number = len(grid)
        temp = [-1 for _ in range(number)]
        for i in range(number):
            count = 0
            # 统计的是每行最后一个数开始连续零的个数count(如果最后一个数是1，则count = 0)
            for j in range(number):
                if grid[i][j]:
                    count = 0
                else:
                    count = count + 1
            # 这个value值表示的是当前第i行在满足要求的二进制网格中行数的位置
            value = number - 1 - count
            # 判断当前的value是否超出了数组的界限
            if value < 0:
                value = 0
            # 这种情况表示的是grid中可能存在多个count值相同的行，我们需要把这个多余的count降低一行
            # (因为第i行的要求的count个数要比第i-1行少一个) 再进行判断，如果降低一行还是不行，继续降低，
            # 直到找到一行，如果没有找到，则说明这个grid
            # 排成不了符合要求的网格
            if temp[value] != -1:
                vv = 0
                for k in range(number - count, number):
                    if temp[k] == -1:
                        vv = 1
                        temp[k] = i
                        break
                # 没有找到，说明无法是grid网格符合要求
                if vv == 0:
                    return -1
            else:
                temp[value] = i
        kk = 0
        # 再利用冒泡排序计算需要temp数组中位置交换的次数即可
        for i in range(number):
            for j in range(number - 1 - i):
                if temp[j] > temp[j + 1]:
                    kk += 1
                    key = temp[j]
                    temp[j] = temp[j + 1]
                    temp[j + 1] = key
        return kk
