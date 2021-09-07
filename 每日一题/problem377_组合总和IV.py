from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 该方法最终超时，我是有点懵的，怎么回溯也开始通过不了了嘛。
        n = len(nums)
        ans = []
        nums.sort()
        # 可以先排个序好搞点。

        def backtrace(cur, path, summ):
            if summ == target:
                ans.append(cur.copy())
                return
            for i, value in enumerate(path):
                if summ + value > target:
                    break
                cur.append(value)
                summ += value
                backtrace(cur, path, summ)
                cur.pop()
                summ -= value
        backtrace([], nums, 0)
        return len(ans)

    def combinationSum4_2(self, nums: List[int], target: int) -> int:
        # 动态规划来做试试
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1   # target 为 0时有一种组合方法啊，那就是没有元素添加吗，()
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        return dp[target]


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 3]
    target = 4
    ans = solu.combinationSum4_2(nums, target)
    print(ans)
