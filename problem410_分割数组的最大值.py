"""
410. 分割数组的最大值
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
注意:
数组长度 n 满足以下条件:
1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:
输入:
nums = [7,2,5,10,8]
m = 2
输出:
18
解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
"""
# 题目的意思就是把数组分成m组，然后要达到所有数组的和中最大值是所有情况中最小的
# 这道题我最初自己想的时候想到了应该会有动态规划解法，可还是想不出来怎么递推公式
# 「将数组分割为 mm 段，求……」是动态规划题目常见的问法。
from typing import List
import sys


class Solution:
    def splitArray(self, nums: List[int], m: int)->int:
        n = len(nums)
        dp = [[sys.maxsize] * (m+1) for _ in range(n+1)]
        sub = [0]
        for num in nums:
            sub.append(sub[-1] + num)

        dp[0][0] = 0
        for i in range(1,n+1):
            for j in range(1, min(i,m)+1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i]-sub[k]))
        return dp[n][m]
# 方法二：二分查找 + 贪心
# 思路及算法
# 「使……最大值尽可能小」是二分搜索题目常见的问法。
# 本题中，我们注意到：当我们选定一个值 x，我们可以线性地验证是否存在一种分割方案，满足其最大分割子数组和不超过 x。策略如下：
# 贪心地模拟分割的过程，从前到后遍历数组，用 sum 表示当前分割子数组的和，cnt 表示已经分割出的子数组的数量（包括当前子数组），
# 那么每当 sum 加上当前值超过了 x，我们就把当前取的值作为新的一段分割子数组的开头，并将 cnt 加 1。遍历结束后验证是否cnt 不超过 mm。
# 这样我们可以用二分查找来解决。二分的上界为数组 nums 中所有元素的和，下界为数组 nums 中所有元素的最大值。通过二分查找
# 我们可以得到最小的最大分割子数组和，这样就可以得到最终的答案了。
# 大致意思就是我们不确定答案，但是知道答案的范围在数组最大值和数组总和之间，那么我们二分查找，也就是每次都猜一个数，然后每次判断这个数是否能够满足
# 存在一种分割方案满足最大分割子数组和不超过这个数，如果满足，那么我们就可以确定答案小于等于这个数啦
    def splitArray_2(self, nums: List[int], m:int) -> int:

        def check(x:int) -> bool:
            # check函数主要用于测试x是否存在满足题意的分割方案
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    total = num
                    cnt += 1
                else:
                    total += num
            return cnt <= m  # 注意判断是否满足分割方案的判断条件，因为如果x很大的话，并不会分割出m个小组，那么其实也算是满足的

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left




solu = Solution()
nums = [7,2,5,10,8]
m = 2
ans = solu.splitArray(nums, m)
print(ans)
