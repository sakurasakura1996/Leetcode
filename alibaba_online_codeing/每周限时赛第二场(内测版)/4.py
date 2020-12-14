"""
排序方案
对于有一个排好序的数组，它的元素可以从队首或者队尾加入或弹出，即双端队列。
每当我们需要插入一个元素，并且保持它是排好序的，可以不断选择做三种操作之一
从队首或队尾弹出一个元素。
将待插入元素加入到队首或队尾。
将之前弹出的元素重新加入到队首或队尾。
每插入一个元素后要保持队列是递增的。
现在给你一个待插入元素的数组，请按顺序插入到一个空数组中，并计算出最少操作次数。
待插入的数组nums的长度为n，1 <= n <= 10^5, 数组中的每个数字各不相同，1 <= numi <= n
示例
输入：
[1,3,4,2]
输出：
6
说明：
1: [] -> [1]
3: [1] -> [1,3]
4: [1,3] -> [1,3,4]
2: [1,3,4] -> [3,4] -> [2,3,4] -> [1,2,3,4]
"""
# 本题考察的是树状数组/线段树的应用，我们不需要模拟数组实际的插入过程
# 如果使用二分查找，找到对应的位置，然后模拟插入的话，时间复杂度会退化到O(N^2)
# 对于第 i 个数的插入，我们可以认为前 i - 1 个数已经排好序了，只需考虑先将前缀取出，还是先将后缀取出。
# 所以我们需要统计前 i - 1 个数中比当前数小的个数，以及比当前数大的个数。采取较小的方案即可。
# 代码思路 树状数组(Binary Indexed Tree(B.I.T), Fenwick Tree)是一个查询和修改复杂度都为log(n)的数据结构。
# 主要功能有修改数组某一位的值和查询前缀和。
# 某个数加上它的 lowbit，即他的二进制最低位 1 的位的二次幂，可以找到它对应节点的父节点。
# 某个数减去它的 lowbit，可以找打计算前缀和时的下一位置，直到减到零为止。
# 复杂度分析
#   设待插入的数组长度为 N。
# 时间复杂度
#   树状数组每次插入和查询的时间复杂度为 O(logN)。总时间复杂度为 O(NlogN)。
# 空间复杂度
#   树状数组的空间复杂度为 O(N)。
from collections import deque


class Solution:
    """
    @param nums: the array of elements to be inserted.
    @return: return the least operation number.
    """

    def sortedArrangement(self, nums):
        n = len(nums)
        # 树状数组
        binary_index_tree = [0] * (n + 1)
        result = 0

        for i, number in enumerate(nums):
            # 先获取前缀中比当前数小的个数
            prefix_smaller_count = self.query(number - 1, binary_index_tree)
            # 计算前缀中比当前数大的个数
            prefix_larger_count = i - prefix_smaller_count

            # 计算结果，采取更小的方案
            result += 2 * min(prefix_smaller_count, prefix_larger_count) + 1

            # 将当前数也加入树状数组中, 在number位置上+1，代表number出现过
            self.update(number, 1, binary_index_tree)

        return result

    def lowbit(self, x):
        return x & (-x)

    # 更新position位置上的值，使其加上value
    def update(self, position, value, binary_index_tree):
        while position < len(binary_index_tree):
            binary_index_tree[position] += value
            position += self.lowbit(position)

    # 查询[1,position]所有值的和
    def query(self, position, binary_index_tree):
        prefix_sum = 0
        while position > 0:
            prefix_sum += binary_index_tree[position]
            position -= self.lowbit(position)
        return prefix_sum
