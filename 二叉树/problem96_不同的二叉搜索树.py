"""
96. 不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
示例:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
# first solution I thought is 递归
# second solution maybe uses dynamic planning
class Solution:
    def numTrees(self, n: int) -> int:
        # dynamic planning
        if n <= 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += (dp[i-j] * dp[j-1])
        return dp[n]

# 动态规划思路，但是完成的速度实在太慢了点啊，还得加油
# 思路就是我们存储不同数量节点可以组成的搜索树个数，因为有这样一个特征，因为二叉搜索树是有顺序的，所以以x为根节点，那么比x小的在左子树上，
# 而比x大的就在右子树上，并且他们都是连续的数，所以 2,3,4和 4,5,6组成的二叉搜索树数量是一样的啊。
# 对于n个数，它的排列组合无非就是分别以1到n为根节点就行枚举，其中有一个特征就是，确定了以某个值为根节点，那么左子树和右子树的节点个数就是确定的了。
# 只需要利用dp数组存起来不同节点个数可以组成二叉搜索树的结果，在就起来就就行了。
solu = Solution()
ans = solu.numTrees(2)
print(ans)


