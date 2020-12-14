class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # 贪心算法，我们开始全部赋值1，然后从后向前一个一个的变成z，直到不能了，最后的答案结构是 'a'* na + 'b'-'y'+ 'z'*nz
        k -= n   # 全部赋值为1
        z_number = k // 25
        last = k % 25
        ans = 'a' * (n-1-z_number) + (chr(ord('a') + last) if z_number != n else '') + 'z' * z_number
        return ans

    def getSmallestString2(self, n: int, k: int) -> str:
        ans = []
        for rest in range(n, 0, -1):
            bound = k - 26 * (rest - 1)
            if bound > 0:
                ans.append(chr(bound+96))
                k -= bound
            else:
                ans.append('a')
                k -= 1
        return "".join(ans)


solu = Solution()
n = 5
k = 73
ans = solu.getSmallestString2(n, k)
print(ans)
