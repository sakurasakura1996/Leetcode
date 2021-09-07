from typing import List
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 题目的意思可能比较难懂，只要做了某一分工作满足了minProfit就可以了 。也就是找子集
        # 我们先找出能够大于等于minProfit的工作序号，剩下的就是做了也达不到标准，另外需注意还有一类
        # 就是如果 group[i] > n的时候，这个要直接排除掉不能算了。
        # 妈的，完全理解错误题意了，这里的意思是多个工作同时进行，但是总人数不能超过n啊。我吐了。
        mod = pow(10, 9) + 7
        canOver = 0
        cantDabiao = 0  # 收益不够minProfi
        for g, pro in zip(group, profit):
            if g <= n and pro >= minProfit:
                canOver += 1
            else:
                cantDabiao += 1
        # 接下来开始算有多少种
        if canOver == 0:
            return 0
        ans = pow(2, canOver) - 1 % mod
        tmp = pow(2, cantDabiao)
        return ans * tmp

    def profitableSchemes2(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 动态规划，这类题目都是这样的。这么多天的每日一题都是这类动态规划题目。
        m = len(group)
        MOD = 10**9 + 7
        dp = [[[0] * (minProfit+1) for _ in range(n+1)] for _ in range(m+1)]
        # dp数组的含义一定要领会清楚， dp[i][j][k] 表示的是在前i个小组中，当前还能加入j个员工工作，最小利润为k的选择数
        dp[0][0][0] = 1
        for i in range(1, m+1):
            members, pro = group[i-1], profit[i-1]
            for j in range(n+1):
                for k in range(minProfit+1):
                    if j < members:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-members][max(0, k - pro)]
        ans = sum(dp[m][i][minProfit] for i in range(n+1))
        return ans % MOD

if __name__ == '__main__':
    solu = Solution()
    n = 1
    minProfit = 1
    group = [1,1,1,1,2,2,1,2,1,1]
    profit =[0,1,0,0,1,1,1,0,2,2]
    ans = solu.profitableSchemes2(n, minProfit, group, profit)
    print(ans)
