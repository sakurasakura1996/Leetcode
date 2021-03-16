# 要求，不要使用除法，且在 O(n)时间复杂度内完成此题，进阶要求使用常数空间。输出数组不被视为额外空间
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        num = 1
        for i in range(1, n):
            num *= nums[i-1]
            output[i] = num
        print(output)
        num = 1
        for j in range(n-2, -1, -1):
            num *= nums[j+1]
            output[j] = num * output[j]
        return output


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2]
    ans = solu.productExceptSelf(nums)
    print(ans)

