"""
31. 下一个排列
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。
示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]

示例 4：
输入：nums = [1]
输出：[1]
提示：
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
# 看到这题，并没有想到什么常规的解法来解决。然后在纸上画了画，感觉可能发现了规律，如果我们真的把所有排列罗列出来，太慢了，应该会超时啊
# 规律就是，我罗列了个例子，下一个排列时，我们从后往前找到第一个从小到大的对子， 也就是一对数，左边数小于右边数，那么下一个排列就是从左边这个数开始改
# 比如 [1, 2, 3, 4]，从后往前看，第一对数就是 3和4，所以就从3开始改，如果是 [1, 2, 4, 3]，那么就是2和4这一对数，从2开始改动。怎么改动呢，
# 我的想法就是把改动的所有数中排个序，第一个数是比原来的数大的最小数，然后剩下其他的数就是从小到大排列。
# 另外如果是倒序排列了，也就是如果从后往前找，没找到这一对数，那么返回的就是所有数从小到大的排列。
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n == 1:
            return
        cur, pre = n-1, n-2
        # 找到从后往前数，第一个顺序对
        while pre >= 0:
            if nums[cur] > nums[pre]:  # 注意这里应该没有等于号
                break
            pre -= 1
            cur -= 1
        if pre < 0:
            nums.sort()
        else:
            num = nums[pre]
            tmp = nums[pre:].copy()
            tmp.sort()
            for i in range(len(tmp)):
                if tmp[i] > num:
                    idx = i
                    break   # 这里要写break，因为我们要找的是比num大的最小元素哈哈哈

            nums[pre] = tmp[idx]
            nums[pre+1:] = tmp[:idx] + tmp[idx+1:]


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 3, 2]
    solu.nextPermutation(nums)
    print(nums)





