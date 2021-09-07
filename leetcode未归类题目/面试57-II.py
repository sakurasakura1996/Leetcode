"""
和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
"""
# 因为要求输出的是连续序列，所以就发现有一个特点啊：对称的两个数和是一样的。比如  12345，1和5  2和4
# 初步猜测可以根据这个来做
from typing import List

# way 1 暴力法，也通过了，不过用时较多
# class Solution:
#     def findContinuousSequence(self, target: int) -> List[List[int]]:
#         ans_list = []
#         for i in range(1,int(target/2)+1):
#             ans = i
#             p = i
#             while ans<target:
#                 p +=1
#                 ans +=p
#             if ans == target:
#                 ans_list.append([x for x in range(i,p+1)])
#         return ans_list

# way2 枚举+数学优化
# 以way1为基础，如果我们知道起点x和终点y，那么x累加到y的和可以由求和公式计算，那么问题就转化为是否存在一个正整数y>x满足求和公式=target
# 再用初中所学的一元二次方程来求解，我们只需要遍历x，然后分别去求是否有一个y可以满足题目，时间复杂度就是O(target)
# import math
# class Solution:
#     def findContinuousSequence(self, target: int) -> List[List[int]]:
#         ans_list = []
#
#         for i in range(1,int(target/2)+1):
#             delta = 1 - 4*(i-i*i-2*target)
#             if delta < 0:
#                 continue
#             delta_sqrt = math.sqrt(delta)
#             if delta_sqrt * delta_sqrt == delta and (delta_sqrt-1)%2 == 0:
#                 y = int((-1+delta_sqrt)/2)
#                 if i < y:
#                     ans = [x for x in range(i,y+1)]
#                     ans_list.append(ans)
#         return ans_list
# 方法二已经快了很多了，下面介绍方法三 双指针法
# way3 基于方法1暴力枚举，但是方法一没有利用这是一个连续的序列，直接可以用求和公式，时间复杂度只有O(target)
# 另外注意，开始知道双指针法，我第一想到的是两指针放在两端，发现是有矛盾的，如果num>target,那到底是left右移还是right左移呢，所以就不对了
# 而是两指针指在最小的两个数上。
# import math
# class Solution:
#     def findContinuousSequence(self, target: int) -> List[List[int]]:
#         ans_list = []
#         left = 1
#         right =2
#         while left<right:
#             num = (left+right)*(right-left+1)/2
#             if num == target:
#                 ans = [x for x in range(left,right+1)]
#                 ans_list.append(ans)
#                 # 注意很多情况不止一组解，那么找到一组解之后呢，left肯定要右移
#                 left += 1
#                 right += 1
#             elif num < target:
#                 right += 1
#             else:
#                 left += 1
#         return ans_list

# way4 滑动窗口法
# 感觉这个方法和方法三的双指针法是一样的，滑动窗口也是维持一个窗口，两边界就相当于方法三的双指针
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left = 1
        right = 1  # 滑动窗口左闭右开
        sum = 0
        ans_list = []
        while left <= int(target/2):
            if sum < target:
                sum += right
                right += 1
            elif sum > target:
                sum -= left
                left += 1
            else:
                ans = [x for x in range(left,right)]
                ans_list.append(ans)
                sum -= (2*left+1)
                left += 2
        return ans_list



solu = Solution()
ans = solu.findContinuousSequence(15)
print(ans)



