from functools import lru_cache
class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(None)
        def numTree(left, right):
            ans = 0
            if left > right:
                return 1
            if left == right:
                return 1
            for i in range(left, right+1):
                ans += numTree(left, i-1) * numTree(i+1, right)
            return ans

        ans = numTree(1, n)
        return ans

    @lru_cache(None)
    def numTrees2(self, n: int) -> int:
        if n <= 0: return 1
        if n <= 2: return n


        # 为什么这里的写法不对呢，而下面一行的结果是对的，思路不是一摸一样吗。。。
        ans = 0
        for i in range(1, n+1):
            ans += (self.numTrees2(i-1) * self.numTrees2(n-i))
        return ans

        # return sum([self.numTrees(i - 1) * self.numTrees(n - i) for i in range(1, n + 1)])



if __name__ == '__main__':
    solu = Solution()
    ans = solu.numTrees2(19)
    print(ans)


