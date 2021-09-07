## 题目
"""
编辑距离：给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
 
示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
## 分析
"""
这道题我以前做过，但是leetcode不知道为什么没有刷题记录了，正好自己再
来刷一遍试试。这道题用动态规划还是挺明显的。
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    	n1 = len(word1)
    	n2 = len(word2)
    	ans = list(numpy.zeros((n1+1,n2+1)).astype(int))
    	# 注意要把初始值和特殊值先赋值好，不然会出现数组越界
    	ans[0][0] = 0
    	for i in range(1, n1+1):
    		ans[i][0] = i
    	for i in range(1,n2+1):
    		ans[0][i] = i
    	for i in range(1, n1+1):
    		for j in range(1,n2+1):
    			if word1[i-1] == word2[j-1]:
    				ans[i][j] = ans[i-1][j-1]
    			else:
    				ans[i][j] = min(ans[i-1][j-1],ans[i-1][j],ans[i][j-1])+1
    	return int(ans[n1][n2])