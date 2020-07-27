"""
剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
示例 1：
输入：[3,4,5,1,2]
输出：1
示例 2：
输入：[2,2,2,0,1]
输出：0
注意：本题与主站 154 题相同
"""
# 我们可以直接简单的遍历一遍，找到第一个小于前面的数然后返回他
# 但是我们再想想，这个数组原来是排好序的，然后旋转了一下，其实两部分都还是有序的，那么
# 二分查找是不是还是可以用呢，我们要找的数是这个数比左边小，比右边小
# 二分法就放到主站154题去写吧，我去看了下，不一样啊，153和154背景相同，但是难度上升了啊

from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return None
        n = len(numbers)
        for i in range(1,n):
            if numbers[i] < numbers[i-1]:
                return numbers[i]
        return numbers[0]

solu = Solution()
numbers = [2,2,2,0,1]
ans = solu.minArray(numbers)
print(ans)