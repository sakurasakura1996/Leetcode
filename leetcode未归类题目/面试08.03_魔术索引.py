"""
面试题 08.03. 魔术索引
魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，
在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。
示例1:
 输入：nums = [0, 2, 3, 4, 5]
 输出：0
 说明: 0下标的元素为0

示例2:
 输入：nums = [1, 1, 1]
 输出：1
提示:
nums长度在[1, 1000000]之间
"""
# 因为nums长度可能很长，所以直接遍历的方式不是很好，但应该也能通过
from typing import List
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == i:
                return i
        return -1

    def findMagicIndex_2(self, nums:List[int])->int:
        # 还能想到的快点的方法就是二分搜索了，但是这里不是严格的单调递增，所以只能用用二分思想
        def getAnswer(nums:List[int],l,r)->int:
            if l > r:return -1
            mid = (l+r)//2
            left = getAnswer(nums,l,mid-1)
            if left!= -1:
                return left
            elif nums[mid] == mid:
                return mid
            else:
                return getAnswer(nums,mid+1,r)

        ans = getAnswer(nums,0,len(nums)-1)
        return ans


solu = Solution()
nums = [0, 2, 3, 4, 5]
ans = solu.findMagicIndex_2(nums)
print(ans)