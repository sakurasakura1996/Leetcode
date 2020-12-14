"""
739. 每日温度
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""
from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 现在这道题能做出来的话，也是因为我今天做了三四到单调栈的题目，然后在已知这道题用单调栈的方法的前提下可以做出来，那么以后呢
        # 所以，我们还是得多总结啊，什么题目我们可以想到单调栈呢：题目中明显的字眼就是某元素左边或者右边第一个比它大或者比它小的元素的位置或者值
        n = len(T)
        ans = [0] * n

        stack = list()
        # 找右侧第一个比该元素大的值，那么我们就要从右向左遍历，维护递减栈
        # 要注意stack中存储的是值还是索引值，这里理解之后应该是索引值更加适合
        for i in range(n-1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            ans[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return ans


if __name__ == '__main__':
    solu = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    ans = solu.dailyTemperatures(T)
    print(ans)