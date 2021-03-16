"""
448. 找到所有数组中消失的数字
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
示例:
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
"""
from typing import List
from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 先不考虑复杂度问题，用想到的方法解决问题 O(n)时间复杂度， O(n)空间复杂度
        nums_counter = Counter(nums)
        ans = []
        n = len(nums)
        for i in range(n):
            if i+1 not in nums_counter:
                ans.append(i+1)
        return ans

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        # 还是要按照题目要求来做。做到O(1)空间复杂度
        # 大致可以发现，数组元素在 1 到 n之间，那么我们是否可以将数组元素和索引值联系起来呢
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            nums[idx] = -1 * abs(nums[idx])
        ans = []
        for i in range(n):
            if nums[i] > 0:
                ans.append(i+1)
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [4,3,2,7,8,2,3,1]
    ans = solu.findDisappearedNumbers2(nums)
    print(ans)




