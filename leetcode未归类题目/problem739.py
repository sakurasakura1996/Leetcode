"""
739.每日温度
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""

# 想不出简化方法，先用暴力法做一个
# way1 暴力法（超时）
# from typing import List
# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#
#         T_len = len(T)
#         ans = [0] * T_len
#         for i in range(T_len):
#             if i == T_len-1:
#                 ans[i] = 0
#             elif T[i] < T[i+1]:
#                 ans[i] = 1
#             else:
#                 for j in range(i+1, T_len):
#                     if T[j] > T[i]:
#                         ans[i] = j-i
#                         break
#
#         return ans
# 显然，暴力法超时了。那么想想还有什么其他简便方法。

# way2 好吧 没做出来，得注意下这题，感觉没那么好想到啊，题目意思理解起来倒是不难
# 题解中的暴力法是可以解决问题的，因为他的负责度是O(MN)。M相当于【30，100】的长度
# N相当于数组长度，而我上面的方法复杂度最差是O（N2）所以数组长度很长的时候，还是差很多
# 题解中的暴力法：
"""
由于温度范围在 [30, 100] 之内，因此可以维护一个数组 next 记录每个温度第一次出现的下标。数组 next 中的元素初始化为无穷大，在遍历温度列表的过程
中更新 next 的值。反向遍历温度列表。对于每个元素 T[i]，在数组 next 中找到从 T[i] + 1 到 100 中每个温度第一次出现的下标，将其中的最小下标记为
 warmerIndex，则 warmerIndex 为下一次温度比当天高的下标。如果 warmerIndex 不为无穷大，则 warmerIndex - i 即为下一次温度比当天高的等待
 天数，最后令 next[T[i]] = i。
为什么上述做法可以保证正确呢？因为遍历温度列表的方向是反向，当遍历到元素 T[i] 时，只有 T[i] 后面的元素被访问过，即对于任意 t，当 next[t] 
不为无穷大时，一定存在 j 使得 T[j] == t 且 i < j。又由于遍历到温度列表中的每个元素时都会更新数组 next 中的对应温度的元素值，因此对于任意 t，
当 next[t] 不为无穷大时，令 j = next[t]，则 j 是满足 T[j] == t 且 i < j 的最小下标。
"""
# 感觉这个暴力法还是挺难想的，是自己太弱了吗，哭了。。。
# from typing import List
# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         n = len(T)
#         ans, nxt, big = [0]*n, dict(), 10**9
#         for i in range(n-1, -1, -1):
#             warmer_index = min(nxt.get(t, big) for t in range(T[i]+1, 102))
#             if warmer_index != big:
#                 ans[i] = warmer_index - i
#             nxt[T[i]] = i
#         return ans

# 下面的解法才是最应该关注的，单调栈方法。
# 维护一个存储下标的单调栈，从栈底到栈顶的下标对应的温度列表中的温度依次递减。
from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        ans = [0]*length
        stack = []
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans






solu = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
ans = solu.dailyTemperatures(temperatures)
print(ans)
