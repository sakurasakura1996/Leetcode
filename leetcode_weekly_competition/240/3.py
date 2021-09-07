from typing import List
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        # 数组 left 初始化为 0，数组right 初始化为 n-1
        # 设置为元素不存在时的特殊值
        left, right = [0] * n, [n-1] * n
        # 单调栈
        s = list()
        for i, num in enumerate(nums):
            while s and nums[s[-1]] >= num:
                # 这里的right是非严格定义的，right[i]是右侧最近的小于等于nums[i]的元素下标
                right[s[-1]] = i - 1   # 这里这样写 可读性比较差啊，他这里这样写的原因就是防止数组越界这些问题，right右边界-1
                # left 左边界 + 1，到时候计算的时候注意还原回去就行了。right这里为什么要取等于号呢
                s.pop()
            if s:
                # 这里的left 是严格定义的，left[i]是左侧最近的严格小于nums[i]的元素下标
                left[i] = s[-1] + 1
            s.append(i)
        # 前缀和
        pre = [0]
        print(left)
        print(right)
        for i, num in enumerate(nums):
            pre.append(pre[-1] + num)
        best = max((pre[right[i]+1] - pre[left[i]]) * num for i, num in enumerate(nums))
        return best % mod

    def maxSumMinProduct2(self, nums: List[int]) -> int:
        # 纸上得来终觉浅
        # 左右添加两个哨兵，方便单调栈的判断
        nums = [0] + nums + [0]
        # 前缀和
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)

        # 右边第一个比当前元素小的元素位置
        rightLower = [None] * len(nums)
        leftLower = [None] * len(nums)
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] >= num:
                # 出栈, 终于搞懂了为什么上面是大于等于了，因为如果nums数组中有两个连续的3，我们要寻找严格大小关系的元素，所以等于要出栈的
                rightLower[stack.pop()] = i
            if stack:
                leftLower[i] = stack[-1]
            stack.append(i)
        print(preSum)
        print(leftLower)
        print(rightLower)
        ans = 0
        for i in range(1, len(nums)-1):
            # 这里的下标关系有点乱，不太好搞清楚啊
            cur = nums[i] * (preSum[rightLower[i]] - preSum[leftLower[i]+1])
            ans = max(ans, cur)
        return ans % (10 ** 9 + 7)

if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 3, 2 ]
    ans = solu.maxSumMinProduct2(nums)
    print(ans)