"""
机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下
移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] 
因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1

提示：
1 <= n,m <= 100
0 <= k <= 20
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 这个题目，我先想到的是，注意，比如坐标为（9，9)时，如果m=n=10,且 k = 8这种的话，那么(9,9),(9,10),(10,9)都不能访问，但是
# （10，10）是可以访问的，但是访问不到，被挡住了哦。
# 初步看了第一感觉就是深度优先或者广度优先

import numpy as np
from typing import List
def visit(x:int, y:int, k:int, jvzhen:List[List[int]], m:int, n:int) -> int:
	ans = 0
	step_dict = {0:[-1,0],1:[1,0],2:[0,-1],3:[0,1]}  # 对应上下左右
	for i in range(4):
		loc_x = x
		loc_y = y	
		if (loc_x+step_dict[i][0])>=0 and (loc_x+step_dict[i][0])<m and (loc_y+step_dict[i][1])>=0 and (loc_y+step_dict[i][1])<n:			
			num = sum([int(a) for a in str(loc_x + step_dict[i][0])])+sum([int(b) for b in str(loc_y+step_dict[i][1])])
			if num<=k and jvzhen[loc_x + step_dict[i][0]][loc_y+step_dict[i][1]] == 0:
				ans +=1
				loc_x = loc_x + step_dict[i][0]
				loc_y = loc_y + step_dict[i][1]
				jvzhen[loc_x][loc_y] = 1
				ans += visit(loc_x,loc_y,k,jvzhen,m,n)
	return ans


class Solution:
	def movingCount(self, m: int, n: int, k: int) -> int:
		jvzhen = np.zeros((m,n)).astype(int)
		jvzhen[0][0] = 1
		ans = visit(0,0,k,jvzhen,m,n)
		return ans+1
    	

solu = Solution()
ans = solu.movingCount(3,1,0)
print(ans)





