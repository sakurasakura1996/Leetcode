# 22.括号生成
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 这个题目自己没想出来。看了题解之后还是没那么难想的啊。第一个位置必须是左括号，那么一定有一个右括号对应，
# (a)b那么a和b就是答案的子集了，那么我们就会发现其中的递归方法了。
from typing import List

# 方法一
# class Solution:
# 	def generateParenthesis(self, n:int) -> List[str]:
# 		if n==0:
# 			return ['']
# 		ans = []
# 		for c in range(n):
# 			for left in self.generateParenthesis(c):
# 				for right in self.generateParenthesis(n-c-1):
# 					ans.append('({}){}'.format(left,right))
# 		return ans


# 方法二:动态规划  思想其实和上面方法基本相同.
class Solution:
	def generateParenthesis(self, n:int) -> List[str]:
		if n==0:
			return [""]
		dp = [None for _ in range(n+1)]  # 注意不是dp=[]
		# 初始值赋值
		dp[0] = [""]
		for i in range(1,n+1):
			cur = []
			for j in range(i):
				left = dp[j]
				right = dp[i-j-1]
				for s1 in left:
					for s2 in right:
						cur.append("("+s1+")"+s2)
			dp[i] = cur
		return dp[n]

# 方法三 深度优先遍历
from typing import List
class Solution:
	def generateParenthesis(self, n:int)-> List[str]:
		res = []
		cur_str = ''

		def dfs(cur_str, left, right):
			"""
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
            	res.append(cur_str)
            	return
            if right<left:
            	return
            if left>0:
            	dfs(cur_str+'(',left-1,right) 
            if right>0:
            	dfs(cur_str+')',left,right-1)
            dfs(cur_str, n,n)
            return res


solu = Solution()
ans = solu.generateParenthesis(3)
print(ans)
