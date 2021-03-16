from collections import defaultdict
class Solution:
    def f(self, n, d, m):
        # n为台阶数，d为List[int]存储地雷台阶，m为List[List[int]]存储传送门
        dp = [0] * (n+1)
        diLei = set(d)
        chuanSong = defaultdict(list)
        for item in m:
            x, y = item[0], item[1]
            chuanSong[y].append(x)
        dp[1] = 1 if 1 not in diLei else 0
        dp[2] = 1 + dp[1] if 2 not in diLei else 0
        for i in range(3, n+1):
            if i in diLei:
                dp[i] = 0
                continue
            elif i in chuanSong:
                # 该位置是传送门的目标位置
                for num in chuanSong[i]:
                    if num != i-1 and num != i-2:
                        dp[i] += dp[num]
            dp[i] = dp[i] + dp[i-1] + dp[i-2]
        return dp


if __name__ == '__main__':
    solu = Solution()
    n = 10
    d = [7]
    m = [[6, 6]]
    ans = solu.f(n, d, m)
    print(ans)

