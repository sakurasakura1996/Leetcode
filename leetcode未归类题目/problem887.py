"""
887.鸡蛋掉落
"""
# 在读了题目之后，主要还是想把数据变成一颗高度最小的平衡二叉树
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
    	if K == 1:
    		return N
    	else:
    		ans = 0
	    	while N>=1 and K>1:
	    		ans +=1
	    		if int(N%2) == 1:
	    			N = int(N/2)+1
	    		else:
	    			N = int(N/2)
	    		print(N)
	    		K -=1
	    	ans = ans + N
    	return ans-1


solu = Solution()
ans = solu.superEggDrop(3, 14)
print(ans)

