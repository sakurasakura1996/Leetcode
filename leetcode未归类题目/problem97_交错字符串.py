"""
97. 交错字符串
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
示例 1:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
"""
class Solution:
    # def isInterleave(self, s1:str, s2: str, s3:str) -> bool:
    #     if not s1:
    #         return s2 == s3
    #     if not s2:
    #         return s1 == s3
    #     s1_len = len(s1)
    #     s2_len = len(s2)
    #     s3_len = len(s3)
    #     if s1_len + s2_len != s3_len:
    #         return False
    #     s1_point = 0
    #     s2_point = 0
    #     s3_point = 0
    #     while s1_point < s1_len and s2_point < s2_len:
    #         if s1[s1_point] == s3[s3_point] and s2[s2_point] != s3[s3_point]:
    #             s1_point += 1
    #             s3_point += 1
    #         elif s2[s2_point] == s3[s3_point] and s1[s1_point] != s3[s3_point]:
    #             s2_point += 1
    #             s3_point += 1
    #         elif s1[s1_point] == s3[s3_point] and s2[s2_point] == s3[s3_point]:
    #             return self.isInterleave(s1[s1_point+1:], s2[s2_point:], s3[s3_point+1]) or self.isInterleave(s1[s1_point:], s2[s2_point+1:], s3[s3_point+1])
    # 上面本来想用双指针来写，好像不太对
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 看完题解之后还是用的动态规划来写，我当时想了如果用动态规划来写该怎么写，可是没有想出来，原因在于没有想到dp数组的具体含义
        # 这时候可以想想研一算法课上老师分析的东西，我们如果要用动态规划来思考问题，就需要分析子问题，从头开始到第i个，或者从末尾到第i个，或者中间部分第i个到第j个这样。
        # 这里的子问题是比较简单的，就是从头开始到第i个。f(i,j)表示s1前i个，s2前j个能够和s3前(i+j)个进行交错字符串，从末尾算起
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        if s1_len + s2_len != s3_len:
            return False
        if s1_len == 0:
            return s2 == s3
        if s2_len == 0:
            return s1 == s3
        dp = [[False]*(s2_len+1) for _ in range(s1_len+1)]
        dp[0][0] = True
        # 初始化边界值
        for i in range(1,s1_len+1):
            dp[i][0] = dp[i-1][0] and (s3[i-1] == s1[i-1])
        for i in range(1,s2_len+1):
            dp[0][i] = dp[0][i-1] and (s3[i-1] == s2[i-1])
        for i in range(1,s1_len+1):
            for j in range(1,s2_len+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]


solu = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
ans = solu.isInterleave(s1,s2,s3)
print(ans)