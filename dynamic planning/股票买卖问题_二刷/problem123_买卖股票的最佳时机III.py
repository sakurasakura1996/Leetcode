from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """题目中的要求变化了，这次只准你交易两次，其实这是交易k次的特殊案列，难度是一样的，后面会有一题是k次交易"""
        n = len(prices)
        if n == 1:
            return 0
        dp = [[[0, 0] for i in range(3)] for _ in range(n)]

        # 这里的边界情况需要搞清楚,我觉得这是这里才是最难想通的地方
        # dp[i][k][1] 表示第i天，我手上持有股票，至今已经交易k次了。
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = 0  # 这里有影响吗，填0和填 -float('inf')并没有什么区别，因为递推公式始终没有用到这部分。

        for j in range(1, 3):
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, 3):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])  # 这里的含义是买入就算用掉了一次交易机会
        return dp[n-1][2][0]

    def maxProfit2(self, prices: List[int]) -> int:
        # 这里我们换种思考方法，只有当卖出去，我们才算完成交易一次,好吧，下面这个方法存在问题。。。。。
        n = len(prices)
        if n == 1:
            return 0
        dp = [[[0, 0] for _ in range(3)] for _ in range(n)]

        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -prices[0]  # 这里要改变了，因为当前第一次买入股票是被允许的了。
            dp[i][2][1] = -float('inf')
        for k in range(2):
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, 3):
                # 我们注意，要定义好dp[i][k][1] 的先后顺序，我们第i天已经有了k次交易，是在今天操作之后已经进行了k次交易机会吗？
                # 同时注意，下面的递推关系相比上面的变化了，所代表的含义不太一样，那么初始化也要相应调整啊
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])  # 我们定义卖出才计算一次花掉一次交易机会
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])
        print(dp)
        return dp[n-1][2][0]


if __name__ == '__main__':
    solu = Solution()
    prices = [2,1,2,0,1]
    ans = solu.maxProfit2(prices)
    print(ans)
