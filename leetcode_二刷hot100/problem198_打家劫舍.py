from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n   # 这里的dp数组定义不同，我定义dp[1]=nums[1]的意思就是，投了第1家所得的最大值，题解中是，总共有1家可以偷的时候所得的最大值
        dp[0] = nums[0]
        dp[1] = nums[1]   # 也可以是 max(nums[0], nums[1])
        ans = max(nums[0], nums[1])
        for i in range(2, n):
            # for j in range(i-1):
            #     dp[i] = max(dp[i], dp[j]+nums[i])
            #     ans = max(ans, dp[i])
            # 没必要上面那么麻烦，太前面的不可能是最优解
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return ans




if __name__ == '__main__':
    solu = Solution()
    nums = [2,7,9,3,1]
    ans = solu.rob(nums)
    print(ans)



