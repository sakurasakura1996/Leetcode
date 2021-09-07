from functools import lru_cache
class Solution:
    """
    这题应该用动态规划写，但是我花了很长时间来写，动态规划的思路倒不是很难写，但是有些坑，总是没有考虑到，这里记录下坑：
    (1) dp[0] = 0 or dp[0] = 1 ? 后面通过报错分析，这里应该填1，因为 递推求解dp[2]的时候，如果 s[0:2]是符和要求的，那么要加上这种情况
        所以dp[0] = 1
    (2) 我们存储 数字 和 字母的对应关系时，数字应该也存成字符，为什么呢， 因为如果存 数字的话， 譬如这种 05，我们在递推判断 int(s[i-1:i])的时候
        原本应该是False的，但是 int("06") = 6结果变成了 True，这里要小心点，我没有好好debug，搞了半天才发现这个问题。
    """
    def numDecodings(self, s: str) -> int:
        # 下面使用回溯方法超时了，卧槽。。。那我们怎么办呢，是不是可以简化步骤，看看能不能解决该问题。
        if not s or int(s[0]) == 0:
            return 0
        start = 1
        ch = 'A'
        num_map = {}
        while start < 27:
            num_map[start] = ch
            start += 1
            ch = chr(ord(ch)+1)
        ans = 0

        def backtrace(cur, path):
            nonlocal ans
            if len(cur) == len(s):
                ans += 1
            if path and int(path[0]) in num_map:
                ch = path[0]
                cur += ch
                path = path[1:]
                backtrace(cur, path)
                cur = cur[:-1]
                path = ch + path
            # 我们要考虑到这样一个问题啊，如果这里判断的是 字符 0，那么我们上面的if 判断就直接跳过了，那么接下来
            elif path and int(path[0]) not in num_map:
                return
            if len(path) >= 2 and int(path[0:2]) in num_map:
                ch = path[0:2]
                cur += ch
                path = path[2:]
                backtrace(cur, path)
                cur = cur[:-2]
                path = ch + path

        backtrace("", s)
        return ans

    def numDecodings2(self, s: str) -> int:
        # 是不是可以用动态规划来写啊。。。。
        # dp[i] 表示的是 s[:i] 有多少种编码方法
        if not s or s[0] == '0':
            return 0
        start = 1
        ch = 'A'
        num_map = {}
        while start < 27:
            num_map[str(start)] = ch
            start += 1
            ch = chr(ord(ch)+1)
        dp = [0] * (len(s)+1)
        # 初始化
        dp[0] = 1   # 注意，这里dp[0]应该为1，别问我为什么。。。
        dp[1] = 1
        for i in range(2, len(s)+1):
            if s[i-1] in num_map:
                dp[i] += dp[i-1]
            if s[i-2:i] in num_map:
                dp[i] += dp[i-2]
        return dp[len(s)]


if __name__ == '__main__':
    solu = Solution()
    s = "2101"   #
    ans = solu.numDecodings2(s)
    print(ans)