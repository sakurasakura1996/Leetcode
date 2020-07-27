"""
5473. 灯泡开关 IV

房间中有 n 个灯泡，编号从 0 到 n-1 ，自左向右排成一行。最开始的时候，所有的灯泡都是 关 着的。

请你设法使得灯泡的开关状态和 target 描述的状态一致，其中 target[i] 等于 1 第 i 个灯泡是开着的，等于 0 意味着第 i 个灯是关着的。

有一个开关可以用于翻转灯泡的状态，翻转操作定义如下：

选择当前配置下的任意一个灯泡（下标为 i ）
翻转下标从 i 到 n-1 的每个灯泡
翻转时，如果灯泡的状态为 0 就变为 1，为 1 就变为 0 。

返回达成 target 描述的状态所需的 最少 翻转次数。

示例 1：

输入：target = "10111"
输出：3
解释：初始配置 "00000".
从第 3 个灯泡（下标为 2）开始翻转 "00000" -> "00111"
从第 1 个灯泡（下标为 0）开始翻转 "00111" -> "11000"
从第 2 个灯泡（下标为 1）开始翻转 "11000" -> "10111"
至少需要翻转 3 次才能达成 target 描述的状态
"""
# 观察几个示例程序我发现了可能是正确的一个规律，那就是从左边开始算，遇到的第一个1开始，然后计算从这个1到target末尾，有多少段，段的定义就是这段中的数字相同
# 比如“10011”就是三段分别是 1  00  11然后答案就是3，先试试吧
class Solution:
    def minFlips(self, target: str) -> int:
        ans = 1
        n = len(target)
        start = -1
        for i in range(n):
            if target[i] == '1':
                start = i
                break
        if start == -1:
            return 0
        for i in range(start,n):
            if i != start and target[i] != target[i-1]:
                ans += 1
        return ans

solu = Solution()
target = "001011101"
ans = solu.minFlips(target)
print(ans)

