"""
1552. 两球之间的磁力
在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有 n 个空的篮子，
第 i 个篮子的位置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。
已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。
给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。
示例 1：
输入：position = [1,2,3,4,7], m = 3
输出：3
解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。

示例 2：
输入：position = [5,4,3,2,1,1000000000], m = 2
输出：999999999
解释：我们使用位于 1 和 1000000000 的篮子时最小磁力最大。
提示：
n == position.length
2 <= n <= 10^5
1 <= position[i] <= 10^9
所有 position 中的整数 互不相同 。
2 <= m <= position.length
"""
# 题目大致意思就是，想让这些篮球与篮球之间隔得尽量远一些。关键还是最近的篮球距离要实现最大。
# 我最开始的思路就是，因为这里考虑的是篮球之间的距离问题，那我把最开始所有的相邻篮子的距离给计算出来，然后再转化为距离求和使最终的多个值中最小的值最大。
# 说的可能有点懵逼
from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        # num = []
        # n = len(position)
        # for i in range(1,n):
        #     num.append(position[i] - position[i-1])
        # 现在有n-1个距离值，然后我们需要把他们分开，分成m-1个块，前提是块必须是相邻的。我们可以计算总距离，然后除以m-1，这是最大值的可能，然后
        # 不断往下搜索看有没有符合条件的，一旦符合条件就直接输出结果即可
        # sum = sum(num)
        if m == 2:
            return position[-1] - position[0]
        right = position[-1] - position[0]
        left = min([(position[i+1] - position[i]) for i in range(len(position) - 1)])
        # end是最大的可能值，如果不能找到这种方案，那肯定就不行了啊。关键就在这个如果检查这个start是否能够满足
        # 别人的题解用的是二分查找，找到答案的左右边界，左边界是num数组的最小值，右边界是position最大值减最小值
        def check(diff):
            count = 0
            i, j = 0, 0
            while j < len(position):
                while j < len(position) and position[j] - position[i] < diff:
                    j += 1
                if j < len(position):
                    count += 1
                i = j
            return count >= m-1

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1  # left已经不满足情况了


class Solution2:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = min([(position[i+1] - position[i]) for i in range(len(position)-1)])
        right = position[-1] - position[0]

        def check(diff):
            count = 0
            i, j = 0, 0
            while j < len(position):
                while j < len(position) and position[j] - position[i] < diff:
                    j += 1
                if j < len(position):
                    count += 1
                i = j
            return count >= m-1

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

