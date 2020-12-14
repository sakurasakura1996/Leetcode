""""
679. 24 点游戏
你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。
示例 1:
输入: [4, 1, 8, 7]
输出: True
解释: (8-4) * (7-1) = 24

示例 2:
输入: [1, 2, 1, 2]
输出: False
注意:
除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允许的。
你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。
"""
# 困难题每次看到，最困难的就是不知道想不出应该用什么方法什么思路来试试看。无从下手。
# 可不可以用一个蠢方法。def check(nums, target) 检查nums是否可以组成target值，然后把四个数字分开来写。
# 比如 [3, 4, 5, 6] 那么我可以看 check(nums, 8) check(nums, 21) check(nums, 1/8)等等
# 应该不行，因为有括号的问题，如果没有括号应该可行，前两个数用了括号咋办呢。

# 官方题解
# 一共4个数，三个运算符操作。因此可能型非常有限。一共多少种可能性呢
# 首先 4 个数中有序地选出2个数，共有4*3=12中选法，并选择+ - * / 四种运算操作之一，用得到的结果取代选出的2个数字，剩下3个数字
# 然后再剩下的三个数字中有序的选择2个数字，共有 3*2=6中选法，并选择4种运算操作之一，用得到的结果取代选出的2个数字，剩下2个数字
# 最后剩下2个数字，有2种不同顺序，并选择4个运算操作之一
# 因此 总共有 12*4*6*4*2*4 = 9216种不同可能性
# 可以通过回溯的方法遍历所有不同的可能性。可以通过回溯的方法遍历所有不同的可能性。具体做法是，使用一个列表存储目前的全部数字，每次从列表中
# 选出 2 个数字，再选择一种运算操作，用计算得到的结果取代选出的 2 个数字，这样列表中的数字就减少了 1 个。重复上述步骤，直到列表中只剩下
# 1 个数字，这个数字就是一种可能性的结果，如果结果等于24，则说明可以通过运算得到 24。如果所有的可能性的结果都不等于 24，则说明无法通过运算得到24。
# 实现时，有一些细节需要注意。
#   除法运算为实数除法，因此结果为浮点数，列表中存储的数字也都是浮点数。在判断结果是否等于24时应考虑精度误差，这道题中，误差小于10 ** −6可以认为是相等。
#   进行除法运算时，除数不能为0，如果遇到除数为0的情况，则这种可能性可以直接排除。由于列表中存储的数字是浮点数，因此判断除数是否为0时应考虑精度误差，
#   这道题中，当一个数字的绝对值小于10 ** −6 时，可以认为该数字等于0。
# 还有一个可以优化的点。
# 加法和乘法都满足交换律，因此如果选择的运算操作是加法或乘法，则对于选出的 2 个数字不需要考虑不同的顺序，在遇到第二种顺序时可以不进行运算，直接跳过。

from typing import List
class Solution:
    def judgePoine24(self, nums: List[int]) -> bool:
        target = 24
        epsilon = 1e-6
        add, multiply, sub, div = 0, 1, 2, 3

        def solve(nums: List[float]) -> bool:
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - target) < epsilon
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                # 省略重复计算
                                continue
                            if k == add:
                                newNums.append(x+y)
                            elif k == multiply:
                                newNums.append(x*y)
                            elif k == sub:
                                newNums.append(x - y)
                            elif k == div:
                                if abs(y) < epsilon:
                                    continue
                                newNums.append(x / y)
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False
        return solve(nums)


solu = Solution()
nums = [4, 1, 8, 7]
ans = solu.judgePoine24(nums)
print(ans)


