"""
1475.商品折扣后的最终价格
给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。
商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，其中 j 是满足 j > i 且 prices[j] <= prices[i] 
的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。
请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。
示例 1：
输入：prices = [8,4,6,2,3]
输出：[4,2,4,2,3]
"""
# 现在做这种简单题，慢慢的开始想到的不仅仅是暴力法了，奥里给
# 这里我想做的是双指针，left，right，如果prices[right]<left,那么就把left索引位置的值给更新，否则right继续往右
from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        prices_len = len(prices)
        if prices_len == 1:
            return prices
        for i in range(prices_len-1):
            for j in range(i+1, prices_len):
                if prices[i] >= prices[j]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices
# 妈的，还是写的暴力法，
# 看题解有一个单调栈的方法，好像记得上面也有一题用到了单调栈，现在去看看，应该是
# 面试题27，二叉树的镜像问题。这类问题可以用单调栈来解决的特征大概是：
# 我们需要用单调栈来对题目中的某种变量维持一个顺序。拿这题来说，如果说告诉你要用单调栈，那我们
# 来想想，应该构造一个怎样的栈结构呢？如果后面的数大于前面，那就不能直接得到答案，这个时候
# 就需要栈来保存记录，所以栈顶的数是最大的，应该维持一个从栈底到栈顶从小到大的栈
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack =[]
        ans = [prices[i] for i in range(n)]
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                ans[stack[-1]] -= prices[i]
                stack.pop()
            stack.append(i)
        return ans

solu = Solution()
prices = [8,7,4,2,8,1,7,7,10,1]
ans = solu.finalPrices(prices)
print(ans)