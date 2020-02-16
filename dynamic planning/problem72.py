"""
编辑距离
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

字符串的问题很多都可以用动态规划来解决，而且用的还是二维数组。动态规划还是那老三步。
1.定义数组元素的含义
2.找出关系数组元素间的关系式
3.找出初始值
"""
import numpy as np
class Solution:
    def minDistance(self,word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        ans = list(np.zeros((n1+1, n2+1)).astype(int))   # 注意数组的大小是（n1+1，n2+1）
        ans[0][0] = 0
        for i in range(1, n1+1):
            ans[i][0] = ans[i-1][0]+1
        for i in range(1, n2+1):
            ans[0][i] = ans[0][i-1]+1
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                # 这里要判断下 第i个和第j个字符是否相同
                if word1[i-1] == word2[j-1]:   # 一定要注意这里都要减1，不然会报错
                    ans[i][j] = ans[i-1][j-1]
                else:
                    ans[i][j] = min(ans[i-1][j-1], ans[i-1][j], ans[i][j-1])+1
        return ans[n1][n2]

word1 = "intention"
word2 = "execution"
solu = Solution()
ans = solu.minDistance(word1, word2)
print(ans)

