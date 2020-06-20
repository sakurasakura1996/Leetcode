"""
1025 除数博弈
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。
只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。
示例 1：
输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。
"""
# 如果用数学分析的话，确实很简单，就是偶数，先手肯定赢，奇数先手输
# 这道题记录一下是因为可以用动态规划来写。
# dp[i] 表示轮到这个人了，现在黑板上数字上是N

class Solution:
    def divisorGame(self, N: int) -> bool:
        ans = [0 for _ in range(N+1)]
        ans[1] = 0
        if N <= 1:
            return False
        else:
            ans[2] = 1
            for i in range(3, N+1):
                for j in range(1,i//2):
                    if i%j == 0 and ans[i-j] == 0:
                        ans[i] = 1
                        break
            return ans[N] == 1


solu = Solution()
ans = solu.divisorGame(5)
print(ans)

