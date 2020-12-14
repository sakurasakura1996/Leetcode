"""
518. 零钱兑换 II
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
示例 1:
输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2:
输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。

示例 3:
输入: amount = 10, coins = [10]
输出: 1
注意:
你可以假设：
0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数
"""
# 如果知道是动态规划的问题的话，最好联系动态规划的步骤来做。
# 上面的题目转成背包问题就是：有一个背包容量为amount，有一系列物品coins，每个重量为coins[i]，数量无线，请问有多少种方法，能够恰好装满背包
# 1.第一步明确两点， 状态 和 选择。状态有两个 就是背包容量 和 可选择的物品，选择就是装进背包或者不装进背包。背包问题就是这个套路，然后按照模板来做吧
# 2.第二部要明确 dp数组的含义：有两个状态的话，一般用二维数组都可以解决问题啦。dp[i][j]定义为：若只使用前i个物品，当背包容量为j时，有多少种方法恰好装满
# 3.确定base case，也就是二维dp数组的边界情况，dp[0][...]=0  dp[...][0]=1,我们最终想得到的答案就是dp[N][amount],其中N为coins数组的大小。
# 4.然后根据选择，来思考状态转移的逻辑。注意我们这里的问题特殊在物品数量无限，所以和之前有所不同，
from typing import List
class Solution:
    def change(self, amount:int, coins: List[int])->int:
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)]
        # 边界初始化
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]] if j - coins[i-1] >=0 else dp[i-1][j]
        return dp[n][amount]


solu = Solution()
amount = 10
coins = [10]
ans = solu.change(amount, coins)
print(ans)


