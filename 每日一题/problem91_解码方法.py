from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        # 此种方法超时了。
        num_to_str = {}
        for i in range(1, 27):
            num_to_str[str(i)] = chr(ord('A')+(i-1))
        ans = 0

        def backtrace(cur, path):
            nonlocal ans
            if len(cur) == len(s):
                ans += 1
                return
            if len(path) > 0 and path[0] in num_to_str:
                cur += path[0]
                tmp = path[1:]
                backtrace(cur, tmp)
                cur = cur[:-1]
            if len(path) > 1 and path[0:2] in num_to_str:
                cur += path[:2]
                tmp = path[2:]
                backtrace(cur, tmp)
                cur = cur[:-2]
        backtrace("", s)
        return ans

    def numDecodings2(self, s: str) -> int:
        # 动态规划来写写看， dp[i]表示的是前i个字符串的结果
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        num_to_str = {}
        for i in range(1, 27):
            num_to_str[str(i)] = chr(ord('A') + (i - 1))
        for i in range(2, n+1):
            if s[i-1] in num_to_str:
                dp[i] += dp[i-1]
            if s[i-2:i] in num_to_str:
                dp[i] += dp[i-2]
        return dp[n]


if __name__ == '__main__':
    solu = Solution()
    ans = solu.numDecodings2("226")
    print(ans)