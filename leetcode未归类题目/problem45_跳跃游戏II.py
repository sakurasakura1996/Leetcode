from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 从后往前dp可以吗
        n = len(nums)
        if not nums:
            return 0
        dp = [float('inf')] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            if nums[i] == 0:
                continue
            else:
                for j in range(1, nums[i]+1):
                    if i+j >= n:
                        continue
                    dp[i] = min(dp[i], 1+dp[i+j])
        return dp[0]


if __name__ == '__main__':
    solu = Solution()
    nums = [2, 1]
    ans = solu.jump(nums)
    print(ans)

