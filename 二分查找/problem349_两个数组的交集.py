
from typing import List
# 找出两个两个数组的交集，交集中每个元素唯一
# 这道题我不知道为什么要用二分法，感觉用hash存起来不是更快吗
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        ans = []
        set1 = set()
        set2 = set()
        for num1 in nums1:
            set1.add(num1)
        for num2 in nums2:
            set2.add(num2)
        for num1 in set1:
            if num1 in set2:
                ans.append(num1)
        return ans

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 不用set的原因可能意思是花了内存，如果不用内存的话，但是二分法最起码要求有序啊，题中的数组没有顺序啊。
        # 原来题目 说的是排序+双指针，可是我理解的方法一的时间复杂度应该是 O（max（N，M））,为什么题解中说是O(M+N)呢，感觉不对啊，这里还是写一下排序+双指针吧
        nums1.sort()
        nums2.sort()
        length1, length2 = len(nums1), len(nums2)
        ans = []
        idx1 = idx2 = 0
        while idx1 < length1 and idx2 < length2:
            num1 = nums1[idx1]
            num2 = nums2[idx2]
            if num1 == num2:
                if not ans or num1 != ans[-1]:
                    ans.append(num1)
                idx1 += 1
                idx2 += 1
            elif num1 < num2:
                idx1 += 1
            else:
                idx2 += 1
        return ans




if __name__ == '__main__':
    solu = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    ans = solu.intersection(nums1, nums2)
    print(ans)


