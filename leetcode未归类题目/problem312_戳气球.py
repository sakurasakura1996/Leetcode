"""
312. 戳气球
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。
这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
求所能获得硬币的最大数量。
说明:
你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:
输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
# 难度为hard，写不出来啊，竟然可以用动态规划来写我擦
from typing import List
class Solution:
    def maxCoins(self, nums:List[int]) -> int:
        n = len(nums)
        ans = [[0] * (n+2) for _ in range(n+2)]
        val = [1] + nums + [1]

        for i in range(n-1, -1, -1):  # 注意这里一定要是倒序的呀
            for j in range(i+2, n+2):
                for k in range(i+1, j):
                    total = val[i] * val[k] * val[j]
                    total += ans[i][k] + ans[k][j]
                    ans[i][j] = max(ans[i][j], total)
        return ans
    # 题解中给出了记忆化搜索的方法，有一个缓存的方法可以注意注意
    # 我们观察戳气球的操作，发现这会导致两个气球从不相邻变成相邻，使得后续操作难以处理。于是我们倒过来看这些操作，将全过程看作是每次添加一个气球。
    # 我们定义方法solve，令 solve(i,j) 表示将开区间(i,j)内的位置全部填满气球能够得到的
    # 最多硬币数。由于是开区间，因此区间两端的气球的编号就是 i 和 j，对应着 val[i] 和 val[j]。
    def maxCoins_2(self, nums:List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]
        from functools import lru_cache

        @lru_cache(None) # LRU算法：最近最少使用算法  这是python的缓存机制 problem146 LRU缓存机制有点类似考这个
        def solve(left:int, right:int) -> int:
            if left >= right - 1:
                return 0
            best = 0
            for i in range(left+1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left,i) + solve(i,right)
                best = max(best, total)
            return best

        ans = solve(0,n+1)
        return ans





solu = Solution()
nums = [3, 1, 5, 8]
ans = solu.maxCoins(nums)
print(ans)
