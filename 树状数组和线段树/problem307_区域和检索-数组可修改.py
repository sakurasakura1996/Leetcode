"""
problem_307.区域和检索-数组可修改
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。

示例:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
说明:

数组仅可以在 update 函数下进行修改。
你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-mutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class SegmentTree:
    def __init__(self, arr, merge):
        '''
        arr: 传入的数组
        merge: 处理的业务逻辑，例如求和/最大值/最小值，lambda表达式
        '''
        self.arr = arr
        self.n = len(arr)
        # 申请4倍arr长度的空间来存储线段树的节点，
        self.tree = [None] * (4 * self.n)
        # 索引i的左孩子索引为2*i+1，右孩子索引为2*i+2
        self._merge = merge
        if self.n:
            self._build(0, 0, self.n - 1)

    def query(self, ql, qr):
        '''
        返回区间[ql,...,qr]的值
        '''
        return self._query(0, 0, self.n - 1, ql, qr)

    def update(self, index, value):
        # 将arr数组index位置的值更新为value，然后递归更新线段树中被影响的各节点的值
        self.arr[index] = value
        self._update(0, 0, self.n - 1, index)

    def _build(self, tree_index, l, r):
        '''
        递归创建线段树
        :param tree_index: 线段树节点在数组中位置，这个位置是线段树数组的索引位置
        :param l: 该节点表示的区间的左边界， 这个左边界是原数组arr中的位置
        :param r: 该节点表示的区间的右边界， 这个右边界是原数组arr中的位置
        '''
        if l == r:
            self.tree[tree_index] = self.arr[l]
            return
        mid = (l + r) // 2  # 区间中点，对应左孩子区间结束后，右孩子区间开头
        left, right = 2 * tree_index + 1, 2 * tree_index + 2  # tree_index的左右子树索引
        self._build(left, l, mid)
        self._build(right, mid + 1, r)
        # 下面这个merge操作就更加广泛了，这里的求和，下次遇到比如求最大最小值，只需要更改这个merge操作参数就ok啦。代码通用性较高
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])

    def _query(self, tree_index, l, r, ql, qr):
        '''
        递归查询区间[ql,..,qr]的值
        tree_index : 某个根节点的索引
        l, r : 该节点表示的区间的左右边界
        ql, qr: 待查询区间的左右边界
        仔细思考一下，为什么我们要计算原数组arr某一个区间[ql-qr]内的数组和时，需要用到这个根节点索引和该节点表示的区间边界呢
        因为我们计算原数组的区间和时，通过线段树结构的话，还是需要找到这个区间具体被分配到哪些树节点的负责范围内去了，所以从整棵树
        的根节点开始，不断递归的查找。
        '''
        if l == ql and r == qr:
            return self.tree[tree_index]

        # 一定要多注意区分代码中两种区间边界的索引。容易混乱。
        mid = (l + r) // 2  # 区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = tree_index * 2 + 1, tree_index * 2 + 2
        if qr <= mid:
            # 查询区间全在左子树
            return self._query(left, l, mid, ql, qr)
        elif ql > mid:
            # 查询区间全在右子树
            return self._query(right, mid + 1, r, ql, qr)

        # 查询区间一部分在左子树一部分在右子树
        return self._merge(self._query(left, l, mid, ql, mid),
                           self._query(right, mid + 1, r, mid + 1, qr))

    def _update(self, tree_index, l, r, index):
        '''
        tree_index:某个根节点索引
        l, r : 此根节点代表区间的左右边界
        index : 更新的值的索引
        '''
        if l == r == index:
            self.tree[tree_index] = self.arr[index]
            return
        mid = (l + r) // 2
        left, right = 2 * tree_index + 1, 2 * tree_index + 2
        if index > mid:
            # 要更新的区间在右子树
            self._update(right, mid + 1, r, index)
        else:
            # 要更新的区间在左子树index<=mid
            self._update(left, l, mid, index)
        # 里面的小区间变化了，包裹的大区间也要更新
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])


class NumArray:

    def __init__(self, nums: List[int]):
            self.segment_tree = SegmentTree(nums, lambda x, y: x + y)

    def update(self, i: int, val: int) -> None:
            self.segment_tree.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
            return self.segment_tree.query(i, j)


# 树状数组做法如下
class NumArray_2:
    def __init__(self, nums:List[int]):
        self.B = [0] * (len(nums)+1)
        self.build(nums)

    def lowbit(self, x):
        return x & (-x)

    def build(self,nums:List[int]):
        for i, v in enumerate(nums):
            self.update(i, v)

    # 第index个节点增加val，index从1开始算起
    def update(self, index, val):
        val = val - self.sumRange(index, index)
        index += 1
        while index < len(self.B):
            self.B[index] += val
            index += self.lowbit(index)

    # 求数组A[0..index]的和，包含index
    def get_sum(self, index):
        ans = 0
        while index > 0:
            ans += self.B[index]
            index -= self.lowbit(index)
        return ans

    def sumRange(self, i:int, j:int) -> int:
        # 下面的j+1一定要注意，因为原数组索引是0 - n-1的，而我们的树状数组索引是从1开始算起的
        # 所以，我们求 sum(i,j)时，i，j是针对的原数组，而求的时候是要在树状数组上操作的
        # 所以是 self.get_sum(j+1) - self.get_sum(i+1-1),即下面这样写的。
        return self.get_sum(j+1) - self.get_sum(i)
