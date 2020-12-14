"""
357. 计算各个位数不同的数字个数
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。
示例:
输入: 2
输出: 91
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
"""
from typing import List
class Solution:
    ans = 0
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        def backtrack(nums1:List[int], nums2:List[int], num:int):
            if num == n:
                self.ans += 1
                return

            for nums in nums2:
                if nums == 0 and not nums1:
                    backtrack(nums1, nums2, num+1)
                elif nums not in nums1:
                    nums1.append(nums)
                    backtrack(nums1, nums2, num+1)
                    nums1.remove(nums)
        backtrack([], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
        return self.ans

    # 上面这种写法，有一个地方不对，那就是前面是0开头的数字，都不会被计算在内了。所以我们再加上一个判断条件，
    # 如果nums1中没有数，第一个数是0的话，那么就直接省略点，继续往后。但是上面的方法还是有点慢

    # 下面这种写法，找到了题目其中的规律。所以足够简洁。另外我们要注意这其中的题意，我们是按照实际数学中的数字来算的
    # 比如  0023就是23，0034090就是34090，前者是没有重复的，后者有重复。
    def countNumbersWithUniqueDigits2(self, n: int) -> int:
        if n == 0:
            return 1

        n = min(n, 10)
        res = 10
        cur = 9
        k = 9

        for i in range(2, 1 + n):
            cur *= k
            k -= 1
            res += cur
        return res




if __name__ == '__main__':
    solu = Solution()
    ans = solu.countNumbersWithUniqueDigits(2)
    print(ans)
