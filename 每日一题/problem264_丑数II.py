class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        cur = 1
        if n == 1:
            return 1
        p2 = 0
        p3 = 0
        p5 = 0
        while cur < n:
            tmp = min(2 * ans[p2], 3 * ans[p3], 5 * ans[p5])
            if tmp == 2 * ans[p2]:
                p2 += 1
            if tmp == 3 * ans[p3]:
                p3 += 1
            if tmp == 5 * ans[p5]:
                p5 += 1
            ans.append(tmp)
            cur += 1
        return ans[-1]

if __name__ == '__main__':
    solu = Solution()
    n = 3
    ans = solu.nthUglyNumber(n)
    print(ans)
