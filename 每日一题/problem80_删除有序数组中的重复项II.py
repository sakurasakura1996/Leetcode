from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        num = nums[0]  # 当前重复的数字
        number = 1    # 当前数字出现的次数
        cur = 1    # 当前准备修改的数字索引
        p = 1
        while p < n:
            if nums[p] == num and number < 2:
                nums[cur] = nums[p]
                number += 1
                cur += 1
                p += 1
            elif nums[p] == num and number >= 2:
                number += 1
                p += 1
            elif nums[p] != num:
                nums[cur] = nums[p]
                num = nums[p]
                cur += 1
                p += 1
                number = 1
        print(nums)
        return cur

if __name__ == '__main__':
    solu = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    ans = solu.removeDuplicates(nums)
    print(ans)
