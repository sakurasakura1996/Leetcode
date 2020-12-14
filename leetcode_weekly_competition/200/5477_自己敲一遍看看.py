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
    # 贪心算法，这里能用贪心算法，主要思想就是，我们数一下每一横行，从右往左数有多少个0，然后第一行需要n-1个0，而第二行需要n-2个0，依次罗列下去
    # 直到最后一行是不需要0的，所以我们从上到下开始排，运用贪心原则，比如第一行，我们需要n-1个0，如果本身不满足的话，那就往下找啦，直到找到一个
    # 最近的满足情况，如果没找到就可以直接返回-1了。找到了就知道这一次操作花费了多少次操作次数，同时，注意移动后，每一行的位置发生了变化哦
    def minSwaps(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        zeros_nums = []
        ans = 0

        for i in range(n):
            # 统计每一横行从右到左有多少个连续的0
            j = n - 1
            while j >= 0 and grid[i][j] == 0:
                j -= 1
            zeros_nums.append(n-1-j)

        # 然后在从上到下开始计算，第i行需要从右到左0个数为n-1-i个
        for i in range(n-1):
            need_zeros = n-1-i
            j = i
            while j < len(zeros_nums) and zeros_nums[j] < need_zeros:
                j += 1  # 这里要搞清楚，我是从上到下开始满足要求的，上面对0个数的需求更大，所以找到满足的条件就可以了，因为大的肯定给上面用嘛
            if j == len(zeros_nums):
                # 说明没有找到合适条件
                return -1
            # 否则就是找到了，第j行的可以交换到第i行，那么需要操作的次数为j-i次
            ans += j-i
            # 那么交换的时候，并不是直接交换这两行啊，所以还要模拟两两交换的过程
            while j > i:
                zeros_nums[j], zeros_nums[j-1] = zeros_nums[j-1], zeros_nums[j]
                j -= 1
        return ans

    def minSwaps_2(self, grid:List[List[int]]) -> int:
        # 冒泡的思路感觉比贪心要复杂一点，冒泡的核心思想就是生成一个数组，数组的第i个数表示grid中第i行最终需要被安排到数组中该数这一行。
        # 比如 ans = [3,2,0,1]就表示，第0行需要被安放到第3行，第1行需要被安放到第2行，第2行需要被安放到第0行...最后总共的操作次数就是
        # 冒泡排序的交换次数。思路挺有想法的，但是编码起来感觉有点小吃力，多学习，多敲代码，代码能力是日以继夜的练习才能锻炼出来的啊，加油
        n = len(grid)
        # 统计每一行从右往左0的个数
        temp = [-1 for _ in range(n)]
        for i in range(n):
            count = 0
            # 下面的这个写法导致了程序运行不停止，没看懂为啥会出现这个问题啊，不就是统计从右往左有多少个连续的0吗,卧槽，低级错误，你特么j不减怎么会停止循环吗，
            j = n-1
            while j >= 0 and grid[i][j] == 0:
                count += 1
                j -= 1

            value = n - 1 - count  # value表示的是现在的第i行最终需要被分配到的位置
            # 判断当前的value是否超出了边界
            if value < 0:
                value = 0

            # 然后我们再考虑：那么第i行应该被放到第value行对吧，但是value行如果已经被别人占了呢，也就是说可能第i行之前，可能就有某一行和第i行
            # 0的个数相同，然后被分配到了这一行，那么还可以往下分配，因为越往下，所需的0的个数越来越少啊
            if temp[value] != -1:
                flag = 0
                for k in range(n-count,n):
                    if temp[k] == -1:
                        flag = 1
                        temp[k] = i
                        # 注意搞清楚这里的逻辑不是temp[i] = j，因为我们本来的想法是把第i行给移到第value行的，那么用temp
                        # 存储的时候，我们用的方法应该是，temp数组中第value个数等于i,然后用冒泡排序来排序。
                        break
                # 如果没有找到，说明不满足条件，返回-1了
                if flag == 0:
                    return -1
            else:
                temp[value] = i
        ans = 0
        for i in range(n):
            for j in range(n-i-1):
                if temp[j] > temp[j+1]:
                    ans += 1
                    temp[j],temp[j+1] = temp[j+1], temp[j]
        return ans

        # number = len(grid)
        # temp = [-1 for _ in range(number)]
        # for i in range(number):
        #     count = 0
        #     # 统计的是每行最后一个数开始连续零的个数count(如果最后一个数是1，则count = 0)
        #     for j in range(number):
        #         if grid[i][j]:
        #             count = 0
        #         else:
        #             count = count + 1
        #     # 这个value值表示的是当前第i行在满足要求的二进制网格中行数的位置
        #     value = number - 1 - count
        #     # 判断当前的valu是否超出了数组的界限
        #     if value < 0:
        #         value = 0
        #     # 这种情况表示的是grid中可能存在多个count值相同的行，我们需要把这个多余的count降低一行
        #     # (因为第i行的要求的count个数要比第i-1行少一个) 再进行判断，如果降低一行还是不行，继续降低，
        #     # 直到找到一行，如果没有找到，则说明这个grid
        #     # 排成不了符合要求的网格
        #     if temp[value] != -1:
        #         vv = 0
        #         for k in range(number - count, number):
        #             if temp[k] == -1:
        #                 vv = 1
        #                 temp[k] = i
        #                 break
        #         # 没有找到，说明无法是grid网格符合要求
        #         if vv == 0:
        #             return -1
        #     else:
        #         temp[value] = i
        # kk = 0
        # # 再利用冒泡排序计算需要temp数组中位置交换的次数即可
        # for i in range(number):
        #     for j in range(number - 1 - i):
        #         if temp[j] > temp[j + 1]:
        #             kk += 1
        #             key = temp[j]
        #             temp[j] = temp[j + 1]
        #             temp[j + 1] = key
        # return kk




solu = Solution()
grid = [[0,0,1],[1,1,0],[1,0,0]]
ans = solu.minSwaps_2(grid)
print(ans)
