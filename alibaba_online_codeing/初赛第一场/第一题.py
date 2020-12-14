class Solution:
    """
    @param trees: the positions of trees.
    @param d: the minimum beautiful interval.
    @return: the minimum number of trees to remove to make trees beautiful.
    """
    def treePlanning(self, trees, d):
        # write your code here.
        n = len(trees)
        ans = 0
        trees.sort()
        cur = 0
        for i in range(1,n):
            if trees[i] - trees[cur] < d:
                ans += 1
            else:
                cur = i
        return ans

solu = Solution()
trees = [1,2,3,5,6]
d = 2
ans = solu.treePlanning(trees, d)
print(ans)

