"""
44. 通配符匹配
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。
说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。

示例 3:
输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

示例 4:
输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

示例 5:
输入:
s = "acdcb"
p = "a*c?b"
输出: false
"""
# leetcode 难度为hard的题对我来说好难啊。这道题和 problem10十分相似，但是可能还要简单一点，看来我还是菜啊
class Solution:
    # 此方法叫带记忆的递归。
    def isMatch(self, s: str, p: str) -> bool:
        #去除p中连续的*，只保留一个
        new=''
        for i in range(len(p)):
            if p[i]=='*' and i>0:
                if p[i-1]=='*':
                    continue
            new+=p[i]
        #用哈希表保存状态  self.dp[(s,p)]
        self.dp={}
        self.helper(s, new)
        return self.dp[(s,new)]

    def helper(self,s,p):
        if (s,p) in self.dp:
            return self.dp[(s,p)]
        if p=='*' or s==p:
            self.dp[(s,p)]=True
        elif not s or not p:
            self.dp[(s,p)]=False
        elif p[0]=='?' or s[0]==p[0]:
            self.dp[(s,p)]=self.helper(s[1:], p[1:])
        elif p[0]=='*':
            #匹配0个，匹配多个
            self.dp[(s,p)]=self.helper(s, p[1:]) or self.helper(s[1:], p)
        else:
            self.dp[(s,p)]=False
        return self.dp[(s,p)]


    def imMatch_2(self, s: str, p: str) -> bool:
        # 动态规划为什么自己没有想出来呢
        s_len = len(s)
        p_len = len(p)

        dp = [[False] * (p_len+1) for _ in range(s_len+1)]
        dp[0][0] = True
        # 边界值处理一下
        # dp[i][0]都是false，所以不用改动了
        # dp[0][j]的话只有都是*的时候才能为True
        for i in range(1,p_len+1):
            if p[i-1] == '*' and dp[0][i-1]:
                dp[0][i] = True
            else:
                break
        for i in range(1,s_len+1):
            for j in range(1, p_len+1):
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # 选择替代或者不替代
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]  # 不使用星好就是dp[i][j-1] 使用星号就是dp[i-1][j]
                    # 上面这个式子应该是最难理解的部分，星号代替0个字符的话，那么就是看s前i个字符串和p前j-1个字符串来匹配
                    # 如果星号代替了一个或者多个字符的话，那么有可能星号前面已经发挥作用了，那不就是dp[i-1][j] dp[i-2][j]都有可能已经使用了
                    # 这个星号。所以我们从dp[i-1][j]来获得信息。
        return dp[s_len][p_len]

