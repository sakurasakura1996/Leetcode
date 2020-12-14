"""
5497. 查找大小为 M 的最新分组
给你一个数组 arr ，该数组表示一个从 1 到 n 的数字排列。有一个长度为 n 的二进制字符串，该字符串上的所有位最初都设置为 0 。

在从 1 到 n 的每个步骤 i 中（假设二进制字符串和 arr 都是从 1 开始索引的情况下），二进制字符串上位于位置 arr[i] 的位将会设为 1 。

给你一个整数 m ，请你找出二进制字符串上存在长度为 m 的一组 1 的最后步骤。一组 1 是一个连续的、由 1 组成的子串，且左右两边不再有可以延伸的 1 。

返回存在长度 恰好 为 m 的 一组 1  的最后步骤。如果不存在这样的步骤，请返回 -1 。



示例 1：

输入：arr = [3,5,1,2,4], m = 1
输出：4
解释：
步骤 1："00100"，由 1 构成的组：["1"]
步骤 2："00101"，由 1 构成的组：["1", "1"]
步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
步骤 4："11101"，由 1 构成的组：["111", "1"]
步骤 5："11111"，由 1 构成的组：["11111"]
存在长度为 1 的一组 1 的最后步骤是步骤 4 。
示例 2：

输入：arr = [3,1,5,4,2], m = 2
输出：-1
解释：
步骤 1："00100"，由 1 构成的组：["1"]
步骤 2："10100"，由 1 构成的组：["1", "1"]
步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
步骤 4："10111"，由 1 构成的组：["1", "111"]
步骤 5："11111"，由 1 构成的组：["11111"]
不管是哪一步骤都无法形成长度为 2 的一组 1 。
示例 3：

输入：arr = [1], m = 1
输出：1
示例 4：

输入：arr = [2,1], m = 2
输出：2


提示：

n == arr.length
1 <= n <= 10^5
1 <= arr[i] <= n
arr 中的所有整数 互不相同
1 <= m <= arr.length
"""
# 这道题并没有做出来，但是下面两种思路其实都还是比较正常的思路，只不过各自存在一些问题
# 思路一，确实，新改动的一个字符，左右两边如果是1的话会被影响到，所以我们要对他们进行更新，但是，我们没有必要更新和当前改动字符左右相邻
# 的所有字符串啊，而只需要利用O(1)的时间复杂度来改变左右边界字符的长度，因为中间部分不会用到了。但是题解中的思路是使用双字典来做
# 注释代码较大问题，正确代码为题解中的。
# from typing import List
#
# class Solution:
#     def findLatestStep(self, arr: List[int], m: int) -> int:
#         # 超时了。
#         n = len(arr)
#         if n == 1 and m > 1:
#             return -1
#         dp = [0] * (n + 1)
#         ans = -1
#         for i in range(n):
#             tmp = 1
#             if arr[i] - 1 > 0 and dp[arr[i] - 1] > 0:
#                 tmp += dp[arr[i] - 1]
#             if arr[i] + 1 <= n and dp[arr[i] + 1] > 0:
#                 tmp += dp[arr[i] + 1]
#             dp[arr[i]] = tmp
#             if arr[i] - 1 > 0 and dp[arr[i] - 1] > 0:
#                 # for j in range(arr[i] - 1, arr[i] - 1 - dp[arr[i] - 1], -1):
#                 #     dp[j] = tmp 这里并不需要利用O(N)时间复杂度来让所有字符位置的长度都改变，只需要处理边界就行了。
#                 dp[arr[i]-dp[arr[i]-1]] = tmp
#             if arr[i] + 1 <= n and dp[arr[i] + 1] > 0:
#                 # for j in range(arr[i] + 1, arr[i] + 1 + dp[arr[i] + 1]):
#                 #     dp[j] = tmp
#                 dp[arr[i]+dp[arr[i]+1]] = tmp
#             if m in dp:
#                 ans = i + 1
#         return ans if ans != -1 else -1
#
#     def findLatestStep2(self, arr: List[int], m: int) -> int:
#         if m == len(arr):
#             return len(arr)
#         import bisect
#         start = [0, len(arr) + 1]
#         for i, t in enumerate(arr[::-1]):
#             idt = bisect.bisect(start, t)
#             start.insert(idt, t)
#             if m == start[idt + 1] - start[idt] - 1 or m == start[idt] - start[idt - 1] - 1:
#                 return len(arr) - i - 1
#         return -1

"""
题解链接：
https://leetcode-cn.com/problems/find-latest-group-of-size-m/solution/di-203-chang-zhou-sai-ti-jie-by-suibianfahui-2/
思考点主要在当前位置变成1之后会改变哪些位置的连续1的长度？
分析题目，某个位置变成1之后，最直接的影响就是其左右两边，总有两边连续的1的长度都会变成新的总长度
所以首先我们需要一个字典iToLen,键值对为{i:len},存储某个下标对应的连续1的长度，用于动态更新
其次我们还需要一个反向字典lenToCnt,键值对为{len:cnt},存储当前连续1长度对应的个数，那么每次只要这个字典里m对应的cnt大于0，
就说明仍有连续1长度为m的部分
如果我们在每次把某个位置变成1之后都修改左右两边所有连续1的位置的iToLen字典，这样时间复杂度就是N^2了，会超时
但真的有必要修改所有下标吗? 答案是否定的, 其实我们只需要修改新的连续 1 的起点和终点的 iToLen 字典即可, 因为后面操作里新的 1 的
左右两边绝不可能是当前连续 1 的中间部分, 只需要考虑两个边界就行, 这样就把这部分操作从 O(N)降到了 O(1)
然后就是修改反向字典 lenToCnt 了, 这个也很简单, 就是拿到原来左右两侧连续 1 的长度 left 和 right, 将其对应的值各
减去 left 和 right, 因为这些下标的长度都不再是原来的值了, 然后再把总长度 left+right+1 在 lenToCnt 字典中的值加上 left+right+1 即可
下面代码对必要的步骤有详细的解释, 方便大家理解

"""
from typing import List
from collections import defaultdict


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        lenToCnt = defaultdict(int)
        iToLen = {}
        res = -1
        for index, x in enumerate(arr):
            # 转成以0为起点的下标
            i = x - 1
            # 原来的左侧和右侧的连续1的长度
            left = 0
            right = 0
            # 新的连续1的起点和终点下标, 初始化为当前下标
            start = i
            end = i
            if i - 1 >= 0 and i - 1 in iToLen:
                # 更新左侧长度和起点下标
                left = iToLen[i - 1]
                start -= left
            if i + 1 < n and i + 1 in iToLen:
                # 更新右侧长度和终点下标
                right = iToLen[i + 1]
                end += right
            newlen = left + right + 1
            # 更新iToLen字典, 只需要更新两个边界即可
            iToLen[start] = newlen
            iToLen[end] = newlen
            # 更新lenToCnt字典, 减去旧长度的值, 加上新长度的值
            lenToCnt[left] -= left
            lenToCnt[right] -= right
            lenToCnt[newlen] += newlen
            if lenToCnt[m] > 0:
                # 如果仍有连续1长度为m的部分, 更新最终结果为当前arr下标+1
                res = index + 1
        return res

    def findLatestStep2(self, arr: List[int], m: int) -> int:
        # 当时自己做的时候也想着用逆向，反着来看看是不是可以快一些。第一次出现连续m个1的字符串就可以返回了啊。
        # 还是超时了，这方法本质上和我自己的第一种写法没啥区别啊。
        if m == len(arr):return len(arr)
        n = len(arr)
        length = [n] * (n+1)  # 逆向来的话，最初，所有的字符都是1，那么长度就是arr的长度
        for i in range(n-1, -1, -1):
            num = arr[i]  # 也就是第i步将num索引位置的0改成的1，现在我反过来将其变成0,那么其他于其相邻的字符串长度就需要作出改动
            tmp_len = length[num]
            length[num] = 0
            # 计算出num位置左右端相邻字符串的长度
            left = 0
            right = 0
            cur = num
            while cur + 1 <= n and length[cur+1] == tmp_len:
                right += 1
                cur += 1
            left = tmp_len - right - 1
            for j in range(num+1,num+right+1):
                length[j] = right
            for j in range(num-left,num):
                length[j] = left
            if m in length:
                return i
        return -1

    def findLatestStep4(self, arr: List[int], m: int) -> int:
        # 前10大佬中用python写的解答，这代码也忒简洁了吧。
        # 大佬就是大佬啊，什么时候我可以写出这种代码啊
        if m == len(arr):
            return len(arr)
        import bisect
        start = [0, len(arr) + 1]
        for i, t in enumerate(arr[::-1]):
            # 这里又发现了一个小知识点，bisect.bisect(start,t)的含义就是如果把t放到start有序数组中，保证有序，应该会放到那个索引上，
            # 返回的就是这个索引，但是 t值并没有插入到start列表中哦，bisect.insort(start, t)就是把t插入到start列表中。让其继续有序
            idt = bisect.bisect(start, t)
            start.insert(idt, t)
            # 大佬模拟的逆向的过程，所以开始不会出现连续字符串长度等于m的情况，然后每逆向一步，就会出现新的字符串长度。
            if m == start[idt + 1] - start[idt] - 1 or m == start[idt] - start[idt - 1] - 1:
                return len(arr) - i - 1
        return -1

solu = Solution()
arr = [2, 1]
m = 2
ans = solu.findLatestStep2(arr, m)
print(ans)
