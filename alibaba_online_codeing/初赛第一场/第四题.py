class Solution:
    """
    @param heights: the heights of buildings.
    @param k: the vision.
    @param x: the energy to spend of the first action.
    @param y: the energy to spend of the second action.
    @return: the minimal energy to spend.
    """
    def shuttleInBuildings(self, heights, k, x, y):
        # write your code here.
        n = len(heights)
        dp = [float("inf")] * n
        dp[0] = 0
        # 计算一下，每个楼右侧k栋建筑中比当前高的大楼索引
        from collections import defaultdict
        nums = defaultdict(list)
        for i in range(n-1):
            for j in range(i+1,n):
                if j <= i+k and heights[j] >= heights[i]:
                    nums[j].append(i)
                    break
        for i in range(1,n):
            selection1 = float("inf")
            for value in nums[i]:
                if i - k <= value:
                    selection1 = min(selection1, dp[value]+x)
            selection2 = float("inf")
            selection2 = min(selection2, y+dp[i-1])
            if i > 1:
                selection2 = min(selection2, y+dp[i-2])
            dp[i] = min(selection2,selection1)
        return dp[n-1]


solu = Solution()
heights = [1,5,6,3,3,5]
k = 3
x = 10
y = 6
ans = solu.shuttleInBuildings(heights, k, x, y)
print(ans)



