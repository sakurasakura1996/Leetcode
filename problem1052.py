"""
1052.爱生气的书店老板
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满
意，不生气则他们是满意的。书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
示例：
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
"""
# 这道题和我刚写的上一道题很像，只不过这题加了一点内容，原来是直接在0，1数组上来找到最大长度连续子数组，
# 现在呢，0，1数组对应了另一个数组的数值，现在是让此数组的值更大。原理上来说应该差不多，还是再0，1数组上
# 应用滑动窗口，但是再记录一下最大的顾客满意数.仔细考虑之后，发现这道题还是不同于上一题的，此题难一点，更难充分熟悉解法
from typing import List
from collections import Counter
# class Solution:
#     def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
#         if X == 0:
#             return sum(customers)
#         ans = 0
#         window = Counter()
#         left = 0
#         right = 0
#
#         while right < len(grumpy):
#             cur_ans = ans
#             window[grumpy[right]] += 1
#             cur_ans += customers[right]
#
#             while window[0] > X:
#                 window[grumpy[left]] -= 1
#                 cur_ans -= customers[left]
#                 left += 1
#             right += 1
#             ans = max(ans, cur_ans)
#         return ans
# 总结：上面的写法是有问题的，第一个是这里不是就最大的连续滑动窗口，而是求让数值最大了
# 第二个是 ans的计算方式不对，因为ans不仅仅因该是滑动窗口部分满意的数量


# 换一种思考方法，我们其实就是想找到这样一个窗口，满足的是这个窗口中对应grumpy位置中值为0的索引
# 再对应到customers中，使其和最大的情况。那么我可以直接遍历一遍不就行了吗,但是窗口也要每次遍历一遍
# 那就是O(NX)了，复杂度有点高，不是最低的。
class Solution:
    def maxSatisfied(self, customer: List[int], grumpy: List[int], X:int) -> int:
        if X == 0 or X == len(customer):
            return sum(customer)
        # ans = map(lambda x, y: x*y,customers[0:X],grumpy[0:X])
        max_window = 0
        window = 0
        for i in range(X):
            if grumpy[i] == 1:
                window += customer[i]
        max_window = window
        for i in range(1, len(customer)-X+1):
            # max_tmp = window
            if grumpy[i-1] == 1:
                window -= customer[i-1]
            if grumpy[i+X-1] == 1:
                window += customer[i+X-1]
            max_window = max(max_window, window)

        ans = sum(list(map(lambda x, y: x*(1-y), customer, grumpy))) + max_window
        return ans

solu = Solution()
customer = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
ans = solu.maxSatisfied(customer,grumpy,X)
print(ans)

