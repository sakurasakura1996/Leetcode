"""
5476. 找出数组游戏的赢家
给你一个由 不同 整数组成的整数数组 arr 和一个整数 k 。
每回合游戏都在数组的前两个元素（即 arr[0] 和 arr[1] ）之间进行。比较 arr[0] 与 arr[1] 的大小，
较大的整数将会取得这一回合的胜利并保留在位置 0 ，较小的整数移至数组的末尾。当一个整数赢得 k 个连续回合时，游戏结束，该整数就是比赛的 赢家 。
返回赢得比赛的整数。
题目数据 保证 游戏存在赢家。
注意 前面一个数比后面一个数小的时候，这个后面的数相当于已经赢了一回合了哦
示例 1：
输入：arr = [2,1,3,5,4,6,7], k = 2
输出：5

示例 2：
输入：arr = [3,2,1], k = 10
输出：3
解释：3 将会在前 10 个回合中连续获胜。

示例 3：
输入：arr = [1,9,8,2,3,7,6,4,5], k = 7
输出：9

示例 4：
输入：arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
输出：99
提示：
2 <= arr.length <= 10^5
1 <= arr[i] <= 10^6
arr 所含的整数 各不相同 。
1 <= k <= 10^9
"""


# 首先这里的参数可以很大，我们如果直接从头开始算的话会很慢
# 我们可以直接copy一份排序，然后找到第k大的值。这是最小的边界，答案肯定大于等于它
# 这道题还是搞了半天，最后突然发现符合滑动窗口的一些条件啊。
from typing import List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # 特么是不是要用滑动窗口来写啊。
        # 总结来说，下面的代码还是我错了好几次瞎逼往里面加条件结果碰对了的结果，还是好好分析分析
        arr_len = len(arr)
        if k >= arr_len - 1:
            return max(arr)
        left = 0
        right = 1
        window = 0
        while right < arr_len and window <= k:
            if window == k:
                return arr[left]
            if arr[right] < arr[left]:
                window += 1
                arr.append(arr[right])
                right += 1
                if window >= k:
                    return arr[left]
            else:
                window = 1
                left = right
                right += 1
        return arr[left]

    def getWinner_2(self, arr: List[int], k:int)->int:
        # 这个方法是记录别人的，用的完全模拟比赛过程，我就完全没想着用这个方法写，都怕超时，结果还是能过
        # 这个代码相比自己写的运行慢太多，还是不建议这样写，还是比较高兴的现在想问题不是只能想到暴力解法了
        flag = arr[0]
        MAX = max(arr)
        count = 0
        while True:
            if arr[0] < arr[1]:
                flag = arr[1]
                count = 1
                arr.append(arr[0])
                del arr[0]
            else:
                count += 1
                arr.append(arr[1])
                del arr[1]
            if count == k:
                return flag
            elif flag == MAX:
                return flag

    def getWinner_3(self, arr: List[int], k:int) -> int:
        # 这个写法和我自己的解法大致相似，但是他写的更加可读和清晰一些啊。
        if k >= len(arr): return max(arr)
        temp, n = arr[0], -1
        for i in arr:
            if temp >= i:
                arr.append(i)
                n += 1
            else:
                arr.append(temp)
                temp = i
                n = 1
            if n == k:
                return temp



solu = Solution()
arr = [1,25,35,42,70,68]
k = 3
ans = solu.getWinner(arr,k)
print(ans)
