"""
55.跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以
跳跃的最大长度。判断你是否能够到达最后一个位置

不知道题目中是否可以向右跨越
"""
# from typing import List
# import collections
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#     	n = len(nums)
#     	ans = collections.deque()
#     	ans.append([0,nums[0]])  # 第一位是在nums中的索引位置，第二位是数值
#     	while ans:
#     		idx, num = ans.popleft()
#     		if idx == n-1:
#     			return True
#     		if num == 0:
#     			continue
#     		for i in range(1,num+1):
#     			if idx+i < n:
#     				ans.append([idx+i,nums[idx+i]])
#     	return False
# 上面的方法超出时间限制了，那么我么要想一个比较好的方法了。上面的方法可以理解为BFS
# 那么我们想一想，如果可以到达最后一个位置，那么，肯定是通过前面一个数到达的最后一个数，
# 那么找到这个数，那第一个数是否可以到达这个数呢，如果能的话不就能到达最后一个数了吗
# 体会这个意思感觉有点像递归的感觉啊。那就先来试试 
# from typing import List
# import collections
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#     	m = len(nums)
#     	if m == 1:
#     		return True
#     	for i in range(m-1):
#     		if i+nums[i] >= m-1:
#     			# print(i)
#     			return True and self.canJump(nums[:i+1])
#     	return False
# 好像并没有效果，因为提交之后还是时间超时，我们想想看，复杂度确实还是挺高的。
# 再来试试动态规划吧，我们创建一个一维数组，dp[i]表示是否可以到达第i个位置。最后返回dp[-1]就行了
# from typing import List 
# class Solution:
# 	def canJump(self, nums: List[int]) -> bool:
# 		m = len(nums)
# 		dp = [False] * m
# 		dp[0] = True
# 		if m==1:
# 			return True
# 		for i in range(m-1):
# 			if dp[i]:
# 				for j in range(1,nums[i]+1):
# 					if i+j<m:
# 						dp[i+j] = True
# 		return dp[m-1]
# 晕了，方法正确，但还是超时。
# 看了下官方题解，发现自己真的好蠢啊。题解中用的是贪心法，只需要维护，当前所能到达的最大距离
# 然后遍历一次，不断更新最大距离，只要最后大于数组的长度，就可以了
from typing import List 
class Solution:
	def canJump(self, nums: List[int]) -> bool:
		m = len(nums)
		ans = 0
		for i in range(m):
			if i<= ans:
				ans = max(ans, i+nums[i])
				if ans >= m-1:
					return True
		return False






solu = Solution()
ans = solu.canJump([2,3,1,1,4])
print(ans)


