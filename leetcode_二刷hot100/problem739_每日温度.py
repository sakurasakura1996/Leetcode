from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 暴力法的话，大概率是会超时的
        n = len(T)
        ans = [0] * n
        for i in range(n-1):
            for j in range(i+1, n):
                if T[i] < T[j]:
                    ans[i] = j - i
                    break
        return ans

    def dailyTemperatures2(self, T: List[int]) -> List[int]:
        # 我们想想为什么上面的过程会超时呢，因为我们在固定一个点时，每次都是独立的去往后遍历，这样会重复很多次。
        # 怎么解决呢 这个思路编码不难，但是想很容易想出来或者说想的很顺畅，感觉还是挺难的
        # 思路：我开始有注意到题目中温度范围是30-100，那么如果n平方不行，估计应该要用mn的时间复杂度来通过该题
        # 那关键是我们定义一个带有什么含义的数组有用呢，这里直接说题解中的思路：那就是定义一个数组，用来存储不同温度出现的最小下标
        # 但是不是所有，而是从后往前遍历过程中，我们不断更新这个数组，那么就可以一直得到对的答案
        n = len(T)
        ans, nxt, big = [0] * n, dict(), float('inf')
        for i in range(n-1, -1, -1):
            warmer_idx = min(nxt.get(t, big) for t in range(T[i]+1, 102))  # 这里要是102，因为能取到100，从101开始
            if warmer_idx != big:
                ans[i] = warmer_idx - i
            nxt[T[i]] = i
        return ans

    def dailyTemperatures3(self, T: List[int]) -> List[int]:
        # 什么时候用单调栈，对于这个题目，我在做的时候，就能感觉到，我想用一个东西来维护一个顺序，而不是每次重新遍历，太浪费时间
        # 单调栈应该是这道题目最好的解法，之前我还连做过几道单调栈的题目，现在又都忘了
        # 我们再来记录下 单调栈的功能：
        #   （1）单调递增栈 可以找到坐起第一个比当前数字小的元素
        #   （2）单调递减栈 可以找到左起第一个比当前数字大的元素
        # 我们维护一个单调递减栈，
        n = len(T)
        ans = [0] * n
        stack = []
        for i in range(n):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            stack.append(i)
        return ans


if __name__ == '__main__':
    solu = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    ans = solu.dailyTemperatures2(temperatures)
    print(ans)


