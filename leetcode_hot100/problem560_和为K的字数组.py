"""
560. 和为K的子数组
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :
数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
"""
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 时间复杂度是平方级别的，所以最终结果超时啦。
        n = len(nums)
        cur = [0] * (n+1)
        cur[1] = nums[0]
        ans = 0
        for i in range(2, n+1):
            cur[i] = cur[i-1]+nums[i-1]
        for i in range(n+1):
            for j in range(i):
                if cur[i] - cur[j] == k:
                    ans += 1
        return ans

    def subarraySum2(self, nums: List[int], k: int) -> int:
        # 降低时间复杂度，可不可以用空间换时间，动态规划是不是可以解决问题呢，好像时间复杂度还是一样的
        # 真的是别人的写法很简洁，看着是真的舒服，但是提交还是超时了，毕竟这里的时间复杂度还是平方级
        # nums数组的长度是 20000级别的。
        ans = 0
        n = len(nums)
        for i in range(n):
            tmp = 0
            for j in range(i, -1, -1):
                tmp += nums[j]
                if tmp == k:
                    ans += 1
        return ans

    def subarraySum3(self, nums: List[int], k: int) -> int:
        # 上面两个方法都超时了，回顾一下，第二种方法没有用空间，时间复杂度是平方级，第一种方法我用了
        # 前缀和，为什么还是平方级的复杂度呢，可以优化啊，我们仔细想想看，看完题解之后，我只能说我们做的
        # 不够多，我们计算出前缀和了，然后呢，计算到后面的前缀和时，我们为了查看是否有子数组的和等于k，
        # 还是要遍历数组来查找，这是平方级复杂度的原因，那么我们是否可以不用遍历查找来找到前缀和为某一个值的个数呢
        # 当然可以啊，hash表啊宝贝啊。
        n = len(nums)
        prefix = 0
        ans = 0
        from collections import defaultdict
        hashTable = defaultdict()
        hashTable[0] = 1
        for i in range(n):
            prefix += nums[i]
            if (prefix-k) in hashTable:
                ans += hashTable[prefix-k]
            if prefix in hashTable:
                hashTable[prefix] += 1
            else:
                hashTable[prefix] = 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 1, 1]
    k = 2
    ans = solu.subarraySum3(nums, k)
    print(ans)

