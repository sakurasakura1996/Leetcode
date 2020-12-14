"""
503. 下一个更大元素 II
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，
这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
"""
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 首先肯定可以使用暴力法来解决问题，但是是否会超时就不知道了，也敲一下吧
        n = len(nums)
        nums += nums
        ans = [-1] * n
        for i in range(n):
            cur = i+1
            while cur < 2 * n:
                if nums[cur] > nums[i]:
                    ans[i] = nums[cur]
                    break
                else:
                    cur += 1
        return ans

    def nextGreaterElements2(self, nums: List[int]) -> List[int]:
        # 上面的暴力法通过了，但是时间复杂度较高，这里还是用单调栈的思路来解决。
        n = len(nums)
        nums += nums
        # nums拼凑起来之后，后半部分的结果不能全部取到，前半部分的所有结果都可以取到

        ans = [-1] * n

        stack = list()

        for i in range(2*n-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            # 注意这里，我们取前半部分的结果
            if i < n:
                ans[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 1]
    ans = solu.nextGreaterElements2(nums)
    print(ans)

