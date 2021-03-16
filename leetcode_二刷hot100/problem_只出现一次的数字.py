from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        for key, value in nums_counter.items():
            if value == 1:
                return key
    # 要求使用线性时间复杂度，不使用额外空间，那么上面使用Counter计数器就不满足要求了。
    def singleNumber2(self, nums: List[int]) -> int:
        # 位运算，这里可以使用异或运算来解决问题：
        """
        异或运算有以下三个性质：
        （1）：任何数和0做异或运算都是本身
        （2）任何数和本身做异或运算都是0
        （3）异或运算满足交换律和结合律，这样就可以传递了
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        ans = nums[0]
        for i in range(1, n):
            ans = ans ^ nums[i]
        return ans

if __name__ == '__main__':
    solu = Solution()
    nums = [4,1,2,1,2]
    ans = solu.singleNumber2(nums)
    print(ans)