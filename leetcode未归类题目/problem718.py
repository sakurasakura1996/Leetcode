"""
718.最长重复子数组
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
示例 1:
输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释:
长度最长的公共子数组是 [3, 2, 1]。
说明:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""
# 此题方法较为多，但是我一种方法也没做出来，动态规划和滑动窗口我倒是想到了可能是解题思路，但是无从下手。

# way1 动态规划：比较难想的是dp数组怎么定义啊。看了题解才明白一点点
#　dp[i][j] 表示的是 A[i:] B[j:]中最长公共子数组的长度，而且这个子数组必须以i，j头开始算。
from typing import List
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        A_len = len(A)
        B_len = len(B)
        dp = [[0] * (B_len+1) for _ in range(A_len+1)]
        ans = 0
        for i in range(A_len-1, -1, -1):
            for j in range(B_len-1, -1, -1):
                dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans
# 需要说明的是，这种动态规划方法，空间复杂度一般是可以进行优化的，因为递推公式只用到了前后两个式子，那么我们存储每个状态式子的初始值，然后不断更新即可
# way2 滑动窗口，这个方法我刚看题是有get到这个想法，原因是连续的子数组，这个条件让我想到或许可以用滑动窗口来表示。但是没想出来咋写
# 重复子数组在两个数组中的位置可能不同，这是问题所在，但如果我们知道了开始位置，我们就可以根据它们将A和B进行对齐。
# 如 A = [3, 6, 1, 2, 4]
# 和 B =    [7, 1, 2, 9]
#               |  |
# 此时最长重复子数组在A和B中的开始位置相同，我们就可以对这两个数组进行一次遍历，得到子数组的长度。
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def maxLength(addA: int, addB: int, length:int)-> int:
            # 找到两数组从某个位置对齐后的最大重复子数组
            ret = k = 0
            for i in range(length):
                if A[addA+i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        n, m = len(A), len(B)
        ans = 0
        for i in range(n):
            length = min(m, n - i)
            ans = max(ans, maxLength(i,0,length))
        for i in range(m):
            length = min(n, m-i)
            ans = max(ans, maxLength(0,i,length))
        return ans
# 这个题目用滑动窗口感觉解题思路不是那么顺畅，还是了解一下
# way3 二分查找+哈希
# 这个思路是完全没有概念，看看题解怎么解决的
# 如果数组A和B有一个长度为k的公共子数组，那么它们一定有长度为j<=k的公共子数组，这样我们可以通过二分查找的方法来找到最大的k。
# 而为了优化时间复杂度，在二分查找的每一步中，我们可以考虑使用哈希的方法来判断数组A和B是否存在相同特定长度的子数组
# 算了，这个方法不太熟悉，跳过。这题的主要解题方法还是动态规划，动态规划中，你要想明白的一点就是，当我们定义了dp[i][j]时，一定要想清楚代表的
# 含义，当我们想不明白，dp[i][j]表示的是A[i:]  B[j:]中的最长子数组长度的时候，我们可能会发现，这样说还是不太能推出最长公共子串啊，如果子串
# 不是以一段开始的怎么能计算出来呢，这时候我们就要换一种思路，我们就假设它是以i或者j开头开始公共子串的，因为公共子串i和j总有一个位置是对应上的啊


solu = Solution()
A= [1,2, 4, 6, 7]
B = [3, 2, 4,6]

ans = solu.findLength(A,B)
print(ans)
