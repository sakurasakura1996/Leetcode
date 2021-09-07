"""
167. 两数之和 II - 输入有序数组
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""
from typing import List
from collections import defaultdict
# 这道题虽然不难，但是我没懂是不是可以使用相等的值。我觉得是可以的，因为题目中相同的元素是指同一个数，而两个4则应该说是相等的元素，他们不是同一个
class Solution:
    def twoSum(self, numbers: List[int], target:int) -> List[int]:
        numbers_len = len(numbers)
        numbers_counter = defaultdict(list)

        for i in range(numbers_len):
            if numbers[i] in numbers_counter:
                numbers_counter[numbers[i]].append(i+1)
            else:
                numbers_counter[numbers[i]] = [i+1]

        for i in range(numbers_len):
            if (target-numbers[i]) in numbers_counter:
                if (target-numbers[i]) == numbers[i]:
                    if len(numbers_counter[target-numbers[i]]) > 1:
                        return numbers_counter[numbers[i]][:2]
                    else:
                        continue
                else:
                    return [i+1, numbers_counter[target-numbers[i]][0]]

    def twoSum_2(self, numbers: List[int], target:int) -> List[int]:
        # 上面的写法写的也太麻烦冗杂了。题解中说第一种方法是针对无序数组来做的，并没有用到有序的性质
        # 二分查找：在数组中找到两个数，使得他们的和等于目标值，可以首先固定一个数，然后在二分查找另一个数。暴力法为O(n^2)，这个方法是O(nlogn)
        numbers_len = len(numbers)
        for i in range(numbers_len):
            left = i+1
            right = numbers_len-1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i+1, mid+1]
                elif numbers[mid] < target - numbers[i]:
                    left = mid + 1
                else:
                    right = mid - 1
    def twoSum_3(self, numbers: List[int], target: int)-> List[int]:
        # 双指针法：要搞清楚为什么双指针滤去的情况是肯定不满足的.
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total < target:
                left += 1
            else:
                right -= 1


solu = Solution()
numbers = [2, 7, 11, 15]
target = 9
ans = solu.twoSum(numbers,target)
print(ans)




