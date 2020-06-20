"""
给你一个整数数组 bloomDay，以及两个整数 m 和 k 。
现需要制作 m 束花。制作花束时，需要使用花园中 相邻的 k 朵花 。
花园中有 n 朵花，第 i 朵花会在 bloomDay[i] 天盛开，恰好 可以用于 一束 花中。
请你返回从花园中摘 m 束花需要等待的最少的天数。如果不能摘到 m 束花则返回 -1 。
"""
# from typing import List
# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         n = len(bloomDay)
#         if m*k > n:
#             return -1
#         ans = []
#         for i in range(min(bloomDay), max(bloomDay)+1):
#             while i in bloomDay:
#                 idx = bloomDay.index(i)
#                 ans.append(idx)
#                 bloomDay[idx] = 0
#
#                 if len(ans) >= m*k and self.test(ans, m, k):
#                     return i
#
#     def test(self,ans, m, k):
#         # 给定开花的位置，返回bool 是否可以制作m束花，这里ans的长度已经大于等于m*k了
#         if k == 1:
#             return True
#         left = 0
#         right = k-1
#         num = 0
#         ans.sort()
#         while right < len(ans):
#             if ans[right] - ans[left] == right - left:
#                 num += 1
#                 left += k
#                 right += k
#             else:
#                 left += 1
#                 right += 1
#
#         return num == m
#
# solu = Solution()
# bloomDay = [97, 83]
# m = 2
# k = 1
# ans = solu.minDays(bloomDay,m,k)
# print(ans)
# 上述方法应该是可行的，但是测试用例最后超时了，这个方法还是太蠢了
# 最后看其他人的题解，自己上面写的方法还是有明显可以改进的地方，我的test函数写的挺好，用到了滑动窗口，节省了时间复杂度
# 但是外层函数的for循环不够好，题解中都提到了需要使用二分法。因为如果第i天可行，那么第i+1天肯定也行，如果第i天不行，那么第i-1天肯定还是不行的
# 相当于是一个有序集，我们每查询一天，都需要进行test，那么如何最快查找到这一天呢，那就需要二分法了啊。下面自己再尝试修改上面的代码

from typing import List
class Solution:
    def test(self,ans, m, k):
        # 给定开花的位置，返回bool 是否可以制作m束花，这里ans的长度已经大于等于m*k了
        if k == 1:
            return True
        left = 0
        right = k-1
        num = 0
        ans.sort()
        while right < len(ans):
            if ans[right] - ans[left] == right - left:
                num += 1
                left += k
                right += k
            else:
                left += 1
                right += 1

        return num == m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        left = min(bloomDay)
        right = max(bloomDay)
        while left <= right:
            ans = []
            day = (left+right) // 2
            # ans存储的是第day天，所有开了花的位置集合
            for i in range(n):
                if bloomDay[i] <= day:
                    ans.append(i)
            if len(ans) >= m*k and self.test(ans,m,k):
                right = right - 1
            else:
                left += 1
        return left

# 妈的。还是时间超时，我感觉自己已经简化了，但是还是不行啊。我二分遍历每一个day的时候，都要新生成一个ans数组，然后调用test函数判断这一天是否满足
# 我感觉我现在的这种解法复杂度和我看的这个题解中的是一样的啊，我是在主函数里多了一个O（n），但是题解中的test函数也要一个遍历数组的操作啊。下面是题解

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(day):
            n = len(bloomDay)
            flower = [True if v <= day else False for v in bloomDay]
            s, t = 0, 0
            count = 0
            while t < n:
                if not flower[t]:
                    count += (t - s) // k
                    s = t + 1
                t += 1
            count += (t - s) // k
            return count >= m

        left, right = min(bloomDay), max(bloomDay)
        while left <= right:
            day = (left + right) // 2
            if check(day):
                right = day - 1
            else:
                left = day + 1
        return left if check(left) else -1


solu = Solution()
bloomDay = [1,10,2,9,3,8,4,7,5,6]
m = 4
k = 2
ans = solu.minDays(bloomDay,m,k)
print(ans)

