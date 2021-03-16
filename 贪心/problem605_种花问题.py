"""
605. 种花问题
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。
示例 1：
输入：flowerbed = [1,0,0,0,1], n = 1
输出：true

示例 2：
输入：flowerbed = [1,0,0,0,1], n = 2
输出：false
提示：
1 <= flowerbed.length <= 2 * 104
flowerbed[i] 为 0 或 1
flowerbed 中不存在相邻的两朵花
0 <= n <= flowerbed.length
"""
# 简单的贪心规则，从左向右遍历，如果当前是1，那么目前右侧一定是0，如果当前是0，那么右侧如果是1的话，就不能种植了。如果是0且右侧的右侧还是0，则可以种植
# 简单点说，必须至少有三个连续的0才能种的下去，我甚至可以用滑动窗口来计算每次连续的0个数。
# 虽然是简单题，但是我却提交两次都是错的，还是要想清楚一点，第一次提交发现我想的太蠢了，边界上的0个数不一定要3个啊，
# 然后我把边界情况单独拎出来讨论，这其实挺蠢的，然后还是不对，因为特殊情况 [0]的时候为true
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], k: int) -> bool:
        n = len(flowerbed)
        if flowerbed == [0]: return k<=1
        ans = 0
        for i in range(n):
            # 一定要考虑两侧的情况啊，在端点处的时候只需要两个连续的0就可以种花了啊
            if i == 0 and flowerbed[i] == 0:
                if i+1<n and flowerbed[i+1] == 0:
                    ans += 1
                    flowerbed[i] = 1
            elif i == n-1 and flowerbed[i] == 0:
                if i-1 >=0 and flowerbed[i-1]==0:
                    ans += 1
                    flowerbed[i] = 1
            elif flowerbed[i] == 0 and i-1 >=0 and i+1 <n and flowerbed[i-1] == 0 and flowerbed[i+1]==0:
                ans += 1
                flowerbed[i] = 1
        return k <= ans

    def canPlaceFlowers2(self, flowerbed: List[int], k: int) -> bool:
        # 题解中有一种跳格子的方法，如果遇到1，则下一格一定是0，直接跳两格，如果遇到0，那说明是之前跳过来的
        # 那么上一格肯定是0，现在判断下一格是否是0，是0的话，那就可以种花，然后变成1，再跳两格；如果下一格是1
        # 那么不能种话，就跳三格。
        n = len(flowerbed)
        start = 0
        ans = 0
        while start < n:
            if flowerbed[start] == 0 and start + 1 <n:
                if flowerbed[start+1] == 0:
                    ans += 1
                    flowerbed[start] = 1
                    start += 2
                else:
                    start += 3
            # 还是没有说清楚所有情况，最后末尾0不包含在内
            elif flowerbed[start] == 1:
                start += 2
        return ans >= k

    def canPlaceFlowers3(self, flowerbed: List[int], k: int) -> bool:
        # 这里介绍一种思路很清晰的写法。
        n = len(flowerbed)
        for i in range(n):
            if k <= 0:
                return True
            # 然后列出几种不能种话的情况
            if flowerbed[i] == 1:
                continue
            if i > 0 and flowerbed[i-1] == 1:
                continue
            if i < n - 1 and flowerbed[i+1] == 1:
                continue
            # 可以种花了
            flowerbed[i] = 1
            k -= 1
        return k <= 0


if __name__ == '__main__':
    solu = Solution()
    flowerbed = [1, 0, 0, 0, 1, 0, 0]
    n = 2
    ans = solu.canPlaceFlowers3(flowerbed, n)
    print(ans)

