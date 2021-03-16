class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans = [0] * 46
        for i in range(lowLimit, highLimit+1):
            tmp = 0
            cur = i
            while cur:
                tmp += int(cur%10)
                cur = int(cur/10)
            ans[tmp] += 1
        return max(ans)


if __name__ == '__main__':
    solu = Solution()
    lowLimit = 52603

    highLimit = 87295
    ans = solu.countBalls(lowLimit, highLimit)
    print(ans)