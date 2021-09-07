from typing import List
from collections import Counter
class Solution:
    # 题目意思读着挺麻烦的，我们要从中找到逻辑概念
    # 我们应该这样算:我们每次计算每个元素的和。每次去掉当前和最大的一个元素。
    # 错了错了，这道题竟然可以用动态规划来解题，确实，这道题和打家劫舍系列题目很类似。
    # 题解说的挺详细的。https://leetcode-cn.com/problems/delete-and-earn/solution/shan-chu-bing-huo-de-dian-shu-by-leetcod-x1pu/
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        length = max(nums_counter.keys())
        dp = [0 for _ in range(length+1)]
        # 边界初始化
        dp[1] = 1 * nums_counter[1]
        for i in range(2, length+1):
            dp[i] = max(dp[i-1], dp[i-2] + i * nums_counter[i])
        return dp[-1]

if __name__ == '__main__':
    solu = Solution()
    nums = [2, 2, 3, 3, 3, 4]
    ans = solu.deleteAndEarn(nums)
    print(ans)





