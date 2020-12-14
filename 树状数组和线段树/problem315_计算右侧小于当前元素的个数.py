"""
315. 计算右侧小于当前元素的个数
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
示例：
输入：[5,2,6,1]
输出：[2,1,1,0]
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素
"""
# 很容易想到的解法就是暴力法，然后还有归并解法和树状数组的解法，后两种都不是很会写啊。
from typing import List
class Solution:
    def countSmaller_1(self, nums: List[int]) -> List[int]:
        # 暴力写法,不出所料应该是超时的哈哈哈，不然不可能是hard题了
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            for j in range(i,n):
                if nums[j] < nums[i]:
                    ans[i] += 1
        return ans

    def countSmaller_2(self, nums: List[int]) -> List[int]:
        # 题解中提到这里需要懂如何使用归并排序的方法计算序列的逆序对数。可以参考剑指offer51.数组中的逆序对
        # 现在做完逆序对这道题了。确实再来思考这道题可能有点点思路了，但还是不够熟悉他。
        # 这道题相比逆序对要难一点，因为你要时刻记录每个数目前的答案（表达的意思可能不太清晰，就是数组最终对应的答案，在程序执行过程中要被记录下来）
        # 所以我在这里又传入了一个ans数组，用于时刻记录答案结果值。同时我们还要记录原数组每个数在数组中的位置啊。有点混乱了。。。
        # 总结：总的来说，思路和逆序对很像，但是归并的过程中，数的位置发生了变化，我们需要引入一个新的数组来记录每个数字对应的原数组中的下标，例如：
        # a = [8, 9, 1, 5, 2]  index = [0, 1, 2, 3, 4]排序的时候原数组和这个下标数组同时变化，则排序后我们得到这样的两个数组：
        # a = [1, 2, 5, 8, 9]  index = [2, 4, 3, 0, 1],我们用一个ans数组来存储结果，如果某个元素对应的下标为p，我们只需要在ans[p]上记录即可

        def mergeSort(nums,tmp,l,r,index, tmpIndex, ans):
            # 递归截至条件：
            if l >= r:
                return ans

            mid = (l + r) // 2
            mergeSort(nums, tmp, l, mid, index, tmpIndex, ans)
            mergeSort(nums, tmp, mid+1, r, index, tmpIndex, ans)

            i, j, pos = l, mid+1, l
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    # 那么nums[j]前面的数都给nums[i]贡献了一次。
                    tmp[pos] = nums[i]
                    ans[index[i]] += (j - (mid+1))
                    # index怎么更新有点转不过弯来了,好像还需要一个tempIndex，因为直接更新的话，会影响到其他元素。
                    tmpIndex[pos] = index[i]
                    i += 1
                else:
                    tmp[pos] = nums[j]
                    tmpIndex[pos] = index[j]
                    j += 1
                pos += 1

            while i <= mid:
                # 如果左半区间还没有遍历完的话，那么这里的ans还是要进行加法的
                tmp[pos] = nums[i]
                tmpIndex[pos] = index[i]
                ans[index[i]] += (j-(mid+1))
                i += 1
                pos += 1

            while j <= r:
                tmp[pos] = nums[j]
                tmpIndex[pos] = index[j]
                j += 1
                pos += 1

            # 注意这里一定要把tmpIndex更新到index，tmp更新到nums
            index[l:r+1] = tmpIndex[l:r+1]
            nums[l:r+1] = tmp[l:r+1]

        n = len(nums)
        tmp = [0] * n
        ans = [0] * n
        index = [i for i in range(n)]
        tmpIndex = [i for i in range(n)]
        mergeSort(nums, tmp, 0, n-1, index, tmpIndex, ans)
        return ans





