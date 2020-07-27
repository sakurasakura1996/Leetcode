"""
5453. 所有蚂蚁掉下来前的最后一刻  显示英文描述
通过的用户数 0
尝试过的用户数 0
用户总通过次数 0
用户总提交次数 0
题目难度 Medium
有一块木板，长度为 n 个 单位 。一些蚂蚁在木板上移动，每只蚂蚁都以 每秒一个单位 的速度移动。其中，一部分蚂蚁向 左 移动，其他蚂蚁向 右 移动。

当两只向 不同 方向移动的蚂蚁在某个点相遇时，它们会同时改变移动方向并继续移动。假设更改方向不会花费任何额外时间。

而当蚂蚁在某一时刻 t 到达木板的一端时，它立即从木板上掉下来。

给你一个整数 n 和两个整数数组 left 以及 right 。两个数组分别标识向左或者向右移动的蚂蚁在 t = 0 时的位置。请你返回最后一只蚂蚁从木板上掉下来的时刻。


"""
from typing import List
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # left_ = []
        # right_ = []
        # for i in range(len(left)):
        #     left_.append((-1,left[i]))
        # for i in range(len(right)):
        #     right_.append((1,right[i]))
        # time = 0
        # while left_ and right_:
        #     for l in left_:
        #         l[1] = l[1]+l[0]
        #     for r in right_:
        #         r[1] = r[1] + r[0]
        left_max = 0
        right_max = 0
        if left:
            left_max = max(left)
        if right:
            for i in range(len(right)):
                right[i] = n - right[i]
            right_max = max(right)

        ans = max(left_max, right_max)
        return ans

solu = Solution()
n = 6
left = [6]
right = [0]
ans = solu.getLastMoment(n,left,right)
print(ans)