"""
1375. 灯泡开关 III
房间中有 n 枚灯泡，编号从 1 到 n，自左向右排成一排。最初，所有的灯都是关着的。
在 k  时刻（ k 的取值范围是 0 到 n - 1），我们打开 light[k] 这个灯。
灯的颜色要想 变成蓝色 就必须同时满足下面两个条件：
灯处于打开状态。
排在它之前（左侧）的所有灯也都处于打开状态。
请返回能够让 所有开着的 灯都 变成蓝色 的时刻 数目 。
输入：light = [2,1,3,5,4]
输出：3
解释：所有开着的灯都变蓝的时刻分别是 1，2 和 4 。
5473题，199周赛中有这道题的变形IV
"""
# 在看到这题和5473两道题之后，这类题目的思路还是蛮好想的，主要是观察例题中的规律，其实就是找light数组中有几个倒序排列的数组。
# 然后还有一些例外情况，比如1在数组末尾和最大数在开头的情况。也不对，应该是看到某个位置时如果前面的数是1到n的话，那么就可以组成一个答案
from typing import List
class Solution:
    def numTimesAllBlut(self, light: List[int]) -> int:
        # 这个解法超时了，看来遍历一遍的时间复杂度也不能解题，不对，我这个解法中每次都调用max函数已经不止是O(n)时间复杂度了，太慢了
        n = len(light)
        ans = 0
        for i in range(n-1):
            if max(light[:i+1]) == i+1:
                ans += 1
        return ans+1

    def numTimesAllBlut_2(self, light: List[int]) -> int:
        # 下面的解法才是真实的遍历一遍数组的O(n)时间复杂度
        n = len(light)
        ans = 0
        cur = 0
        maxNum = 0
        while cur < n:
            maxNum = max(maxNum, light[cur])
            if maxNum == cur+1:
                ans += 1
            cur += 1
        return ans


solu = Solution()
light =[1,2,3,4,5,6]
ans = solu.numTimesAllBlut_2(light)
print(ans)

