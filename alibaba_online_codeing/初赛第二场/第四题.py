class Solution:
    """
    @param n: The number of pyramid levels n
    @param k: Possible coordinates k
    @return: Find the sum of the number of plans
    """
    def pyramid(self, n, k):
        # write your code here
        ans = 0
        for i in k:
            cha = n - i
            num = 1
            for j in range(2, n+1):
                num *= j
            ans = ans + num
            ans = ans % (1e9+7)
        return int(ans)/2

solu = Solution()
n = 3
k = [1, 2, 3]
ans = solu.pyramid(n, k)
print(ans)
