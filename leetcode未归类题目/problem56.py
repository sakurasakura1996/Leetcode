from typing import List
class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		# 先拍下顺序，然后再来做
		intervals.sort(key=lambda x: x[0])

		ans = []
		for interval in intervals:
			if not ans or interval[0]>ans[-1][-1]:
				ans.append(interval)
			else:
				ans[-1][-1] = max(interval[1],ans[-1][-1])
		return ans

solu = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
ans = solu.merge(intervals)
print(ans)

