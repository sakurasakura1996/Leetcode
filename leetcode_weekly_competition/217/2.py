from typing import List
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # 单调递增栈
        n = len(nums)
        stack = list()
        stack_len = 0
        for i in range(n):
            while stack and stack[-1] > nums[i] and stack_len + n - i > k: # 注意这两个大于号都没有等于号
                stack.pop()
                stack_len -= 1
            stack.append(nums[i])
            stack_len += 1

        return stack[:k]


solu = Solution()
nums = [18,42,66,8,80,2]
k = 3
ans = solu.mostCompetitive(nums, k)
print(ans)






