"""
再重新写一遍第三题看看能不能写出来
这道题最简单的想法就是，每次卖一个球的时候，选择数量最多的那个球去卖，这肯定是最优解，但如果这样想的话，
解题肯定会超时，因为球的数量和种类都很大。
我们可以确定一个阈值T，数量大于这个阈值T的球，都可以一直卖，直到卖到数量为T。
"""
from typing import List
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        l, r, T = 0, max(inventory), -1
        while l <= r:    # 这里的等于号要加上，不然是错的，仔细体会体会
            mid = (l + r) // 2
            # 如果阈值为mid的话，那么可以有多少个球被卖掉需要计算一下。
            total = sum(ai - mid for ai in inventory if ai >= mid)
            # ai - mid 就说明本来有ai个球，卖到了还剩下mid个球。这第mid个球并没有卖掉
            if total <= orders:
                # 可以卖掉的数量total还不够，所以说明阈值高了，还需要往小的方向改，那么r就减小一点吧
                # 为什么阈值T的赋值要放在这里呢，因为total<=orders这是满足条件的，意思就是说，数量大于阈值T的球都需要吧数目先减到T才行。
                T = mid
                r = mid - 1
            else:
                l = mid + 1
        # 二分法结束之后，我们想现在这个阈值的含义。首先total肯定还是满足 total <= orders.那就是说大于阈值T的所有球的数目都要卖掉
        # 卖掉之后，可能还不够，不够不要紧，下一轮，数量等于阈值的一个一个卖，肯定是够了的，因为如果数量为T的球都卖了一个球变成T-1个球
        # 然而还没有凑齐orders个的话，那么阈值就不是T，而是T+1了。说白了，T就是满足total <= orders 的最大值了。
        rest = orders - sum(ai - T for ai in inventory if ai >= T)
        ans = 0
        for ai in inventory:
            if ai > T:
                ans += (ai + T+1) * (ai - T) // 2
        if rest >= 0:
            ans += rest * T
        return ans % (10**9 + 7)


solu = Solution()
inventory = [2,5]
orders = 4
ans = solu.maxProfit(inventory, orders)
print(ans)



