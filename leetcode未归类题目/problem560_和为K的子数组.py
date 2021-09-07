from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 需要注意数组长度为 [1, 20 000]挺大的奥，一般都需要前缀和保存
        n = len(nums)
        preSum = [0] * (n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]
        ans = 0
        # 如何直接这样暴力遍历的话，还是会超时啊，已经很高的复杂度了啊。
        for i in range(1, n+1):
            for j in range(i, n+1):
                if preSum[j] - preSum[i-1] == k:
                    ans += 1
        return ans

    def subarraySum2(self, nums: List[int], k: int) -> int:
        # 简化时间复杂度啊， 我们用hash表存储前缀和值出现的次数，然后遍历到一个数，我们就计算presum
        # 因为presum - presum2 = k,hash表存储的是presum2出现的次数，那么我们就找 presum-k出现的次数吗
        hashtable = defaultdict()
        hashtable[0] = 1
        preSum = 0
        ans = 0
        for num in nums:
            preSum += num
            if preSum - k in hashtable:
                ans += hashtable[preSum - k]
            hashtable[preSum] = hashtable[preSum] + 1 if preSum in hashtable else 1
        return ans

if __name__ == '__main__':
    solu = Solution()
    nums = [1, 1, 1]
    k = 2
    ans = solu.subarraySum2(nums, k)
    print(ans)