"""
120. 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""
# 到现在为止都没怎么做过贪心算法的题目，这里貌似也不是用贪心来做，有点像用图来做
# 每层都有节点，只有相邻层才有路径到达，同层之间的节点没有连接，要求的就是从开始节点到最后层节点
# 使得路径上的和最小，这道题如果用图来思考的话，应该还是要用有向图的结构来说，那么怎么做呢，BFS，DFS吗
# 我擦，竟然说是最经典的动态规划题，那我就用用动态规划来写吧
from typing import List
class Solution:
    # 动态规划思路的话：dp[i][j]数组的含义就是从顶端到第i层第j个数最小路径和的值
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        triangle_len = len(triangle)
        dp = [[0] * triangle_len for _ in range(triangle_len)]
        dp[0][0] = triangle[0][0]

        for i in range(1,triangle_len):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1,i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        return min(dp[triangle_len-1])

    def minimumTotal_2(self, triangle: List[List[int]]) -> int:
        # 那么我们应该也挺熟悉的了，动态规划中的递推公式中，如果当前值只通过前面一行的值得到
        # 那么我们其实是可以进行空间优化的。上面的方法是O(n^2)的空间复杂度，而题目也说了，O(n)复杂度会更加分哦
        if not triangle:
            return 0
        triangle_len = len(triangle)
        dp = [0] * triangle_len
        dp[0] = triangle[0][0]
        for i in range(1, triangle_len): # 同二维dp不同的是：节省空间时需要从后往前遍历，不然会改动数组值
            dp[i] = dp[i-1] + triangle[i][i]
            for j in range(i-1,0,-1):
                dp[j] = min(dp[j],dp[j-1]) + triangle[i][j]
            dp[0] = dp[0] + triangle[i][0]
        return min(dp)

"""
最后再引用一段官方题解中的比较好的部分。
本题还有一些其它的动态规划方法，例如：
从三角形的底部开始转移，到顶部结束；
直接在给定的三角形数组上进行状态转移，不使用额外的空间。
读者可以自行尝试。如果在面试中遇到类似的题目，需要和面试官进行沟通，
可以询问「是否有空间复杂度限制」「是否可以修改原数组」等问题，给出符合条件的算法。
"""


solu = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
ans = solu.minimumTotal_2(triangle)
print(ans)




        