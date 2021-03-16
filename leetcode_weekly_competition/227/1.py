
from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1 or n == 2:
            return True
        ans = False
        for i in range(n):
            # 排列每次轮转的结果
            flag = True
            cur = nums[i:]+nums[:i]
            for j in range(1, n):
                if cur[j] < cur[j-1]:
                    flag = False
                    break
            if flag:
                return True
        return ans

if __name__ == '__main__':
    solu = Solution()
    nums = [3,4,5,1,2]
    ans = solu.check(nums)
    print(ans)


