from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def isDengcha(num):
            length = len(num)
            if length == 1:
                return False
            if length == 2:
                return True
            num.sort()
            delta = num[1] - num[0]
            for i in range(2, length):
                if num[i] - num[i-1] != delta:
                    return False
            return True


        n = len(l)
        ans = []
        for i in range(n):
            num = nums[l[i]:r[i]+1]
            ans.append(isDengcha(num))
        return ans


solu = Solution()
nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]
ans = solu.checkArithmeticSubarrays(nums, l, r)
print(ans)

