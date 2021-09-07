from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # 试试滑动窗口.....还用什么滑动窗口啊，直接遍历一遍就可以了啊
        n = len(nums)
        ans = nums[0]
        window = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                window += nums[i]
                ans = max(ans, window)
            else:
                window = nums[i]
                ans = max(ans, window)
        return ans

if __name__ == '__main__':
    solu = Solution()
    nums = [12,17,15,13,10,11,12]
    ans = solu.maxAscendingSum(nums)
    print(ans)