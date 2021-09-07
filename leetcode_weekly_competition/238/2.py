from typing import List
from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 错误代码，这里不对。
        nums.sort()
        # 二分法查找到最终的最高频元素
        n = len(nums)
        left = 0
        right = n-1
        ans = 1
        while left <= right:
            mid = left + (right - left) // 2
            cost = sum(nums[mid] - nums[i] for i in range(mid))   # woca,这里想错了啊，为什么一定要从0开始呢，其他数字都是900多，
            # 就第一个数是1，那不是血亏吗
            if cost == k:
                # 是否存在重复元素呢
                ans = mid + 1
                for i in range(mid+1, n):
                    if nums[i] == nums[mid]:
                        ans += 1
                    else:
                        break
                return ans
            elif cost < k:
                left = mid + 1
                ans = max(ans, left)
            elif cost > k:
                right = mid - 1
        return ans

    def maxFrequency2(self, nums: List[int], k: int) -> int:


    def maxFrequency3(self, nums: List[int], k: int) -> int:
        # 这里也没有写对，思路是可以了，滑动窗口是可以解决该问题的。
        nums.sort()
        n = len(nums)
        left = 0
        right = 1
        window = [nums[0]]
        cost = 0
        ans = 0
        while right < n:
            if window and nums[right] == window[-1] and cost <= k:
                window.append(nums[right])
                right += 1
                ans = max(ans, len(window))
            elif window and nums[right] > window[-1] and (cost + len(window) * (nums[right] - window[-1])) <= k:
                window.append(nums[right])
                cost += len(window) * (nums[right] - window[-1])
                right += 1
                ans = max(ans, len(window))
            elif window and nums[right] > window[-1] and (cost + len(window) * (nums[right] - window[-1])) > k:
                cost -= (window[-1] - window[0])
                window = window[1:]
                left += 1
        return ans


    def maxFrequency4(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        ct = Counter(nums)

        left, right = 0, ct[nums[0]]
        to_ret = ct[nums[0]]
        rett = ct[nums[0]]
        kt = 0
        while right < len(nums):
            v_right = nums[right]
            kt += (nums[right] - nums[right - 1]) * rett
            while right < len(nums) - 1 and nums[right] == nums[right + 1]:
                right += 1
                rett += 1
            right += 1
            rett += 1

            while kt > k:
                kt -= v_right - nums[left]
                left += 1
                rett -= 1
            # print(v_right, rett, right, left)
            to_ret = max(to_ret, rett)
        return to_ret

    def maxFrequency5(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_freq = 0
        start = 0
        temp_sum = 0
        for end in range(len(nums)):
            temp_sum += nums[end]
            if (1 + end - start) * nums[end] - temp_sum <= k:
                max_freq = max(max_freq, end - start + 1)
            else:
                temp_sum -= nums[start]
                start += 1

        return max_freq

    def maxFrequency6(self, nums, k):
        # 前缀和 + 滑动窗口
        nums.sort()
        pre = [0]  # 前缀和
        for num in nums:
            pre.append(pre[-1] + num)

        ans = 1
        left = 0
        for right in range(len(nums)):

            # 维护一个窗口，窗口内元素经过不超过k次操作，可全部变为最右端元素
            # 我竟然没有想到可以用前缀和之差来表示一段区间内所花费的cost啊。妙啊
            while nums[right] * (right - left) - (pre[right] - pre[left]) > k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans



if __name__ == '__main__':
    solu = Solution()
    nums = [3,9,6]
    k = 2

    ans = solu.maxFrequency3(nums, k)
    print(ans)