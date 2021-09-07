from collections import defaultdict
class Solution:
    def jump(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * n
        s_dict = defaultdict()
        for i, ch in enumerate(s):
            if ch not in s_dict:
                s_dict[ch] = i

        dp[0] = 0
        for i in range(1, n):
            idx = s_dict.get(s[i], -1)
            if idx == -1:
                dp[i] = min(dp[i], dp[i-1]+1)
            else:
                dp[i] = min(dp[i], dp[i-1]+1, dp[idx]+1)
        print(dp)
        return dp[n-1]


if __name__ == '__main__':
    solu = Solution()
    s = "01237687689098989"
    ans = solu.jump(s)
    print(ans)
