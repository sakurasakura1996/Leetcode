"""
买卖股票的最佳时机

"""

# from typing import List
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # 这题目的意思就是在一个列表中找到最大的后面数与前面数的差值
#         # 先用最笨的方法来做吧
#         max = 0
#         for i in range(len(prices)-1):
#             for j in range(i,len(prices)):
#                 num = prices[j] - prices[i]
#                 if num>max:
#                     max = num
#         return max
# 很明显，上面的解法时间超时了，因为方法实在是太笨的方法了，时间复杂度是O(n²)
# 接下来的题解就很清楚。
"""
这个问题说白了，就是寻找pMin，pMax，满足如下条件：
pMin的位置在pMax左边：pMin<pMax
令插值最大：nums[pMin]-nums[pMax]
结合一个实例分析：Nums =[0,10,3,6,-5,-3,-10]
从左向右一次遍历过程中：
首先，nums[0]=0为第一个最小值，nums[4]=-5为第二个最小值
我们从nums[4]将这个示例分成两部分，即nums[0-3]和nums[4-6]
对左边nums[0-3]来说，
nums[4]在该范围右边，因此不能使用nums[4],只考虑本部分即可。
这个范围内可用的最小值就是分割点nums[0]，
该段内最大差值是该范围内最大值减去nums[0]。
对右边nums[4-6]来说，
由于：num[0]>nums[4]
nums[i]-nums[0]<nums[i]-nums[4]
因此该范围内只会使用nums[4]作为最小值，不会使用num[0]，不用考虑左边。
该段内最大差值是该范围内最大值减去nums[4]。
以此类推，我们只要将数据，根据从左向右遍历过程中出现的每个最小值依次分割，分成若干段，然后寻找每段的最大值，与该段最小值（分割点）做差就是该段中出现的最大差值。所有段中的最大值就是我们要找的答案。

"""
# 用自己的话来说就是，我们根据不同的最小值来将整个数组进行分段，然后计算每段里面的最大收益，就可以了，最后再将每段最大收益中的最大值最为答案输出

from typing import List
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pmin = sys.maxsize   # 表示整数的最大值    # 浮点数最大值可以表示为  float('inf')
        max = 0
        for i in range(len(prices)):
            if prices[i] < pmin:
                pmin = prices[i]
            elif (prices[i] - pmin)>max:
                max = prices[i]-pmin
        return max

a = [7,1,5,3,6,4]
# a = [7,6,4,3,1]
solu = Solution()
ans = solu.maxProfit(a)
print(ans)