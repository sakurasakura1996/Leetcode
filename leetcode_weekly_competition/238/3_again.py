from typing import List
from collections import deque
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = 0
        window = deque()
        cost = 0
        ans = 0
        while right < n:
            if not window:
                window.append(nums[right])
                cost = 0
                right += 1
                ans = 1
            else:
                if nums[right] == window[-1] and cost <= k:
                    window.append(nums[right])
                    right += 1
                elif nums[right] > window[-1] and (cost + len(window) * (nums[right] - window[-1])) <= k:
                    cost += len(window) * (nums[right] - window[-1])
                    window.append(nums[right])
                    right += 1
                elif nums[right] > window[-1] and (cost + len(window) * (nums[right] - window[-1])) > k:
                    # 这里比较关键，突然我并没有从0开始计算，那我这里到底是哪里错了呢。
                    # 如果把nums[right]加入到滑动窗口中去的话，那么就不符合题意了，那么这个时候，我们就需要从左边删除元素，从而能够让nums[right]被划分进来。
                    # 这就是另外一个选择了。
                    cost -= (window[-1] - window[0])
                    window.popleft()
                    left += 1
            ans = max(ans, len(window))
        return ans

    def maxFrequency2(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = 0
        cost = 0
        ans = 0
        while right < n:
            if left == right:
                cost = 0
                right += 1
                ans = 1
            else:
                if nums[right] == nums[right-1] and cost <= k:
                    right += 1
                elif nums[right] > nums[right-1] and (cost + (right - left) * (nums[right] - nums[right-1])) <= k:
                    cost += (right - left) * (nums[right] - nums[right-1])
                    right += 1
                elif nums[right] > nums[right-1] and (cost + (right - left) * (nums[right] - nums[right-1])) > k:
                    # 这里比较关键，突然我并没有从0开始计算，那我这里到底是哪里错了呢。
                    cost -= (nums[right-1]-nums[left])
                    left += 1
            ans = max(ans, right-left)
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [3, 9, 6]
    k = 2
    ans = solu.maxFrequency2(nums, k)
    print(ans)
