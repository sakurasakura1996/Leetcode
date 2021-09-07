from typing import List
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # 把握住里面有一个点：就是贪心，我们在获得相同连线数的时候，肯定连的越靠前越好啊。
        # 感觉最近刷题懈怠了，这道题感觉还挺不错的，但是我没有想到，这道题其实就是考的最长公共子序列啊
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

if __name__ == '__main__':
    solu = Solution()
    nums1 = [2,5,1,2,5]
    nums2 = [10,5,2,1,5,2]
    ans = solu.maxUncrossedLines(nums1, nums2)
    print(ans)

