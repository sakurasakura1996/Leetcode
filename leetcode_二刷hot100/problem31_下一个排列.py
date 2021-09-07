from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 找到最后面的一个顺序对
        n = len(nums)
        if n < 2:
            return
        start = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                start = i
                break
        if start == -1:
            nums.sort()
        else:
            num = nums[start]
            temp = nums[start:]
            temp.sort()
            for i in range(len(temp)):
                if temp[i] > num:
                    idx = i
                    break
            nums[start] = temp[i]
            nums[start+1:] = temp[:idx] + temp[idx+1:]


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 1, 5]
    solu.nextPermutation(nums)
    print(nums)