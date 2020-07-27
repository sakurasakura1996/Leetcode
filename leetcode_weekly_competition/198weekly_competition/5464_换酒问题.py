"""
5464. 换酒问题  显示英文描述
通过的用户数 0
尝试过的用户数 0
用户总通过次数 0
用户总提交次数 0
题目难度 Easy
小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。
如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。
请你计算 最多 能喝到多少瓶酒。
"""
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        cur = numBottles
        while cur >= numExchange:
            ans += cur//numExchange
            cur = cur//numExchange + cur%numExchange
        return ans

solu = Solution()
numBottles = 2
numExchange = 3
ans = solu.numWaterBottles(numBottles, numExchange)
print(ans)