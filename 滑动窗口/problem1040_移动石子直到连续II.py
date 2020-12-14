"""
1040. 移动石子直到连续 II
在一个长度无限的数轴上，第 i 颗石子的位置为 stones[i]。如果一颗石子的位置最小/最大，那么该石子被称作端点石子。
每个回合，你可以将一颗端点石子拿起并移动到一个未占用的位置，使得该石子不再是一颗端点石子。
值得注意的是，如果石子像 stones = [1,2,5] 这样，你将无法移动位于位置 5 的端点石子，因为无论将它移动到任何位置（例如 0 或 3），
该石子都仍然会是端点石子。当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。
要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves] 。
示例 1：
输入：[7,4,9]
输出：[1,2]
解释：
我们可以移动一次，4 -> 8，游戏结束。
或者，我们可以移动两次 9 -> 5，4 -> 6，游戏结束。

示例 2：
输入：[6,5,4,3,10]
输出：[2,3]
解释：
我们可以移动 3 -> 8，接着是 10 -> 7，游戏结束。
或者，我们可以移动 3 -> 7, 4 -> 8, 5 -> 9，游戏结束。
注意，我们无法进行 10 -> 2 这样的移动来结束游戏，因为这是不合要求的移动。

示例 3：
输入：[100,101,104,102,103]
输出：[0,0]
提示：
3 <= stones.length <= 10^4
1 <= stones[i] <= 10^9
stones[i] 的值各不相同。
"""
# 这道题的思路还挺复杂的，做的时候没有想明白啊
# 先看最大值，我们先计算左右端点之间空置的位置有多少？然后，为了移动次数最大，我们每次可以选择左右端点中的一个来往内侧移动，但是选哪个呢？
# 为了使移动次数最多，我们肯定希望每次移动端点时，使失去可选端点的数量越少越好，也就是两侧端点和其相邻的点之间可能会有空位置，但是他们会被放弃使用。
# 所以我们就比较两边哪个空置的少，我们就移动少的那边的端点。接下来，还需要每次都比较一次端点吗，No，仔细想想，第一次计算之后，我们肯定是把端点移动到
# 和它原来相邻的节点的内测相邻的部分，如此下去，我们每次都只会损失一个空置位置。那么最大值的结果其实就是 s1 - s2
# （s1:左右端点之间空置的位置有多少 s1=stones[n−1]−stones[0]+1−n） （s2: min(stones[n−1]−stones[n−2]−1,stones[1]−stones[0]−1)
# 最小值：这里就用到了滑动窗口的方法，因为最终肯定就是连续的n个数字连在一起的。那么滑动窗口从头滑动过去，如果已有数字的数量最多，那么空置的位置就越少
# 那么需要移动的次数也就越少。特例是这样的。  [1, 2, 3, 4, 6]这样的情况需要移动一次，[1,2,3,4,7]这样的就需要移动2次啦
from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        s1 = stones[n - 1] - stones[n - 2] + 1 - n
        s2 = min(stones[n - 1] - stones[n - 2] - 1, stones[1] - stones[0] - 1)
        # 最大值
        max_ans = s1 - s2
        # 最小值
        min_ans = float("inf")
        tmp = 0

        # 下面这部分代码我写不出来，这个逻辑感觉读起来倒是不难，但是我写不出来这么简洁的代码。我肯定会写的比较拖拉
        # 这里编码的关键在于应该以stones数组为主要地位。反正这题很耐人思考，编码逻辑挺复杂度。
        for i in range(n):
            while stones[i] - stones[tmp] + 1 > n:
                tmp += 1
            cost = n - (i - tmp + 1)
            if cost == 1 and stones[i] - stones[tmp] + 1 == n - 1:
                min_ans = min(min_ans, 2)
            else:
                min_ans = min(min_ans, cost)
        return [min_ans, max_ans]

    def numMovesStonesII_2(self, stones: List[int]) -> List[int]:
        # minimum moves
        # 寻找包含最多石子的窗口
        stones.sort()
        n = len(stones)
        i = j = 0
        maxcount, left, count = 0, 0, 0
        while i < n and j < n:
            while j < n and stones[j] - stones[i] < n:
                count += 1
                j += 1
            if maxcount <= count:
                maxcount, left = count, i
            count -= 1
            i += 1
        # 分类讨论
        # 注意这里的讨论。
        if stones[left] + n - 1 not in stones and maxcount == n - 1:  # 1.1
            minn = 2
        else:  # 1.2
            minn = n - maxcount
        # maximum moves
        if maxcount == n - 1 and  (stones[n - 1] - stones[1] == n - 2 or stones[n - 2] - stones[0] == n - 2):
            maxn = stones[n - 1] - stones[0] + 1 - n
        else:  # 2.2
            maxn = max(stones[n - 2] - stones[0], stones[n - 1] - stones[1]) - n + 2

        return [minn, maxn]
