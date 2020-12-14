class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # 试试用动态规划
        if n == 1:return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        length = 0

        def lenthOfnumber(number):
            # 算出数字number的二进制长度
            nonlocal length
            while number >= pow(2, length):
                length += 1
            return length

        for i in range(2, n+1):
            # 只需要知道i的二进制长度就行。
            length = lenthOfnumber(i)
            dp[i] = (dp[i-1] * pow(2, length) + i)%1000000007
        return dp[n]


solu = Solution()
ans = solu.concatenatedBinary(12)
print(ans)
