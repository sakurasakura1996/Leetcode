class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x and y:
            if x % 2 == y % 2:
                x = x >> 1
                y = y >> 1
            else:
                ans += 1
                x = x >> 1
                y = y >> 1
        if x:
            ans += bin(x).count("1")
        if y:
            ans += bin(y).count("1")
        return ans

    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")



if __name__ == '__main__':
    solu = Solution()
    ans = solu.hammingDistance(1, 4)
    print(ans)