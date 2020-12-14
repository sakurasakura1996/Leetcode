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


class Solution:
    def sortedArrangement(self, nums):
        n = len(nums)
        # 树状数组
        binary_index_tree = [0] * (n+1)  # 相比线段树，树状数组可以省下很多空间
        result = 0

        for i, number in enumerate(nums):
            # 先获取前缀中比当前数小的个数
            prefix_smaller_count = self.query(number-1, binary_index_tree)
            # 计算前缀中比当前数大的个数
            prefix_larger_count = i - prefix_smaller_count

            # 计算结果，采取更小的方案
            result += 2 * min(prefix_smaller_count, prefix_larger_count) + 1

            # 将当前数也加入到树状数组中，在number位置上+1，代表number出现过
            self.update(number, 1, binary_index_tree)

        return result

    def lowbit(self, x):
        return x & (-x)

    # 更新position位置上的值，使其加上value
    def update(self, position, value, binary_index_tree):
        while position < len(binary_index_tree):
            binary_index_tree[position] += value
            position += self.lowbit(position)

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



