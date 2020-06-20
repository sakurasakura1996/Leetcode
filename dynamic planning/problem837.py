"""
837.新21点
爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：
爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字。 抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，其中 W 是整数。 每次抽取都是独立的，其结果具有相同的概率。
当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？

示例 1：
输入：N = 10, K = 1, W = 10
输出：1.00000
说明：爱丽丝得到一张卡，然后停止。

示例 2：
输入：N = 6, K = 1, W = 10
输出：0.60000
说明：爱丽丝得到一张卡，然后停止。
在 W = 10 的 6 种可能下，她的得分不超过 N = 6 分。

示例 3：
输入：N = 21, K = 17, W = 10
输出：0.73278
"""

# 第一层想到的是搞一个递归，结果还是搞了大半天，没搞出来，
# class TreeNode:
#     def __init__(self, W: int, val: int, increment: int):
#         self.val = val + increment
#         self.pointer = [self.val for _ in range(W)]
#
#
# class Solution:
#     def diGui(self, node: TreeNode, N: int, K: int, W: int):
#         sum1 = 0
#         sum2 = 0
#         if node.val >= K:
#             if node.val <= N:
#                 sum1 += 1
#             sum2 += 1
#         else:
#             for i in range(W):
#                 node.pointer[i] = TreeNode(W, node.val, i+1)
#                 [a, b] = self.diGui(node.pointer[i], N, K, W)
#                 sum1 += a
#                 sum2 += b
#         return [sum1, sum2]
#
#     def new21Game(self, n: int, k: int, w: int) -> float:
#         root = TreeNode(w, 0, 0)
#         [ans_1, ans_2] = self.diGui(root, n, k, w)
#         ans = ans_1/ans_2
#         return round(ans, 6)


# 看到题解有动态规划之后，发现自己对动态规划还是不够了解啊。还得继续加油，先尝试自己能否分析写出动态规划好吧没写出来
# 看题解：
# 这里的动态规划思想还是和以往不同，这个地方的dp数组不容易想到，dp[i]表示的是，在当前你已有的分数为i时，接下来你继续抓取，分数不少于K时停止，此时
# 不大于N的概率值。
class Solution:
    def new21Game(self, N:int, K:int, W:int)-> float:
        if K==0:
            return 1.0
        dp = [0.0 for _ in range(K+W)]
        # 动态规划中的赋初值部分，dp[K]到dp[N]应该都是1，但是这里就牵扯到，N>=K的，但是N和K+W谁大呢我们可以分别讨论一下，如果N大，那么
        # dp[K] 到 dp[K+W]都是1就行了，如果N小，那么就是dp[K]到dp[N]为1就行了，那也就是dp[k]到 dp[min(N,K+w)]都为1就行了
        for i in range(K,min(N,K+W)+1):
            dp[i] = 1.0
        # 本来就可以直接从dp[k-1]到dp[0]直接都用状态转移方程求解就行了，但是这样的重复计算会比较耗时，因为，每次都是取当前索引的后W个值相加
        # 再除以W，那么我们就想到其实这个和每次都只进行了稍微的变化，我们可以进行修改就让计算次数变少很多啦
        dp[K-1] = float(min(N-K+1, W))/W
        for i in range(K-2, -1, -1):
            dp[i] = dp[i+1] - (dp[i+W+1]-dp[i+1])/W
        return round(dp[0],5)

# 这道题没有用动态规划对于我来说还是比较难想到，尤其是这个dp[i]代表什么意思，并且用到了逆向的动态规划，从后往前递推算出dp数组的值。如果知道用
# 动态规划后,再思考dp[i]的含义时，我一定想成了当N或者K为i时获胜的概率值。这样进行下去的时候就断了思路了。这题虽然是中等难度题，却是个好题。

solu = Solution()
N = 1
K = 0
W = 1
ans = solu.new21Game(N, K, W)
print(ans)