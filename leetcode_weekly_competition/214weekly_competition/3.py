"""
5563. 销售价值减少的颜色球
你有一些球的库存 inventory ，里面包含着不同颜色的球。一个顾客想要 任意颜色 总数为 orders 的球。
这位顾客有一种特殊的方式衡量球的价值：每个球的价值是目前剩下的 同色球 的数目。比方说还剩下 6 个黄球，
那么顾客买第一个黄球的时候该黄球的价值为 6 。这笔交易以后，只剩下 5 个黄球了，所以下一个黄球的价值为 5
（也就是球的价值随着顾客购买同色球是递减的）给你整数数组 inventory ，其中 inventory[i] 表示
第 i 种颜色球一开始的数目。同时给你整数 orders ，表示顾客总共想买的球数目。你可以按照 任意顺序 卖球。
请你返回卖了 orders 个球以后 最大 总价值之和。由于答案可能会很大，请你返回答案对 109 + 7 取余数 的结果。
"""
from typing import List
from functools import lru_cache
class Solution:

    # 感觉我的思路是对了，但是写不出来，通过不了啊
    # 我的二分思路是找到倒序inventory中的某个位置上的数，他前面的数都要减到他这么大，但是他自己呢。不太好表达
    # 其实，更好的方法应该用二分法找到具体的球的数量的阈值，也就是大于这个数量的颜色的球，都减到这个值，但是会超过，就设置nums计数和orders比较
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        left = 0
        right = len(inventory)

        @lru_cache(None)
        def check(num):
            if num == 0:
                return 0
            else:
                return check(num-1) + num * (inventory[num-1] - inventory[num])

        while left < right:
            mid = (left + right) // 2
            if check(mid) < orders:
                left = mid + 1
            else:
                right = mid
        ans = 0
        standrad = inventory[left-1]
        num = 0
        i = 0
        while num < orders:
            while inventory[i] >= standrad and num < orders:
                ans += inventory[i]
                ans = ans % (1e+10 + 7)
                inventory[i] -= 1
                num += 1
            i += 1
        return ans

    def maxProfit2(self, inventory: List[int], orders: int) -> int:
        mod = 10**9 + 7

        # 二分查找T阈值，二分法比较复杂的地方就是边界取不取的问题，仔细分析这里的T，其实这个T值是不取到的。
        l, r, T = 0, max(inventory), -1
        while l <= r:
            mid = (l + r) // 2
            total = sum(ai - mid for ai in inventory if ai >= mid)
            if total <= orders:
                T = mid
                r = mid - 1  # 因为total还不够，说 明我们的mid大了，l只能增加，r只能减小，所以r减小1
            else:
                l = mid + 1

        range_sum = lambda x, y:(x+y) * (y-x + 1) // 2
        rest = orders - sum(ai - T for ai in inventory if ai >= T)

        ans = 0
        for ai in inventory:
            if ai >= T:
                if rest > 0:  # 这里的意思就是，本来值为T时，我们可以不用再减了，但是现在rest大于0，还要剪一个
                    ans += range_sum(T, ai)
                    rest -= 1
                else:
                    ans += range_sum(T+1, ai)
        return ans % mod



solu = Solution()
inventory = [2,8,4,10,6]
orders = 20
ans = solu.maxProfit2(inventory, orders)
print(ans)