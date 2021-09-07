from typing import List
class Solution:
    """
    这道题还可以仔细探究探究啊，题目中这里是升序被拆分成两端升序，升序情况下，我们是不能和nums[left]比对的。那么降序情况下被拆分，是不是
    应该和nums[left]比对了呢，而且和nums[right]比对是错误的。这里我们来实验下。
    """
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] < nums[n-1]:
            return nums[0]
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

    def findMin2(self, nums: List[int]) -> int:
        # 这里将条件设置成降序拆分数组，然后测试是否应该和nums[left]比较才是对的,测试结果发现确实如此啊。
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[left]:
                right = mid - 1
            else:
                left = mid
        return nums[left]



if __name__ == '__main__':
    solu = Solution()
    nums = [3, 2, 1, 5, 4]
    ans = solu.findMin2(nums)
    print(ans)