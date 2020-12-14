from collections import Counter
class Solution:
    """
    @param lengths: the lengths of sticks at the beginning.
    @return: return the minimum number of cuts.
    """
    def makeEquilateralTriangle(self, lengths):
        # write your code here.
        nums = Counter(lengths)
        lengths.sort()
        n = len(lengths)
        ans = float("inf")
        for i in range(n):
            if nums[lengths[i]] >= 3:
                return 0
            elif nums[lengths[i]] == 2 and i != n-2 and i != n-1:
                ans = min(ans, 1)
            elif nums[lengths[i]] == 1 and nums[2*lengths[i]] >= 1:
                ans = min(ans, 1)
            else:
                ans = min(ans, 2)
        return ans


solu = Solution()
leng = [1, 3, 4, 4]
ans = solu.makeEquilateralTriangle(leng)
print(ans)

