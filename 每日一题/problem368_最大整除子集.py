import bisect
from typing import List
from sortedcontainers import SortedList
class Solution:
    # 注意：nums中元素是没有排序的，这没关系，但是我们现在的候选子集，单独存储他们的时候我们可以搞一个有序集合来存储
    # 这样的话，新加入一个元素，我们判断他是否能加入这个子集的时候是否会更容易判断一些（节省效率）。
    # no talk, show my code!
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = 0
        ans = []
        window = []
        max_ans_len = 0
        while right < n:
            if not window:
                window.append(nums[right])
                ans = window.copy()
                max_ans_len = 1
            else:
                # 好像维持有序集合并没有卵用啊，只能在新插入的元素是最小或者最大的时候，可以用O(1)解决
                # 其他情况并不能避免都要算一遍的问题。
                index = bisect.bisect_left(window, nums[right])
                if index == 0:
                    if window[0] % nums[right] or nums[right] % window[0] == 0:
                        bisect.insort(window, nums[right])
                        if len(window) > max_ans_len:
                            ans = nums[left:right]
                            max_ans_len = len(window)
                    else:
                        left = right
                        window.clear()
                elif index >= len(window):
                    if nums[right] % window[-1] == 0 or window[-1] % nums[right] == 0:
                        bisect.insort(window, nums[right])
                        if len(window) > max_ans_len:
                            ans = nums[left:right+1]
                            max_ans_len = len(window)
                    else:
                        left = right
                        window.clear()
                else:
                    flag = True
                    for i in range(len(window)):
                        if window[i] % nums[right] != 0 and nums[right] % window[i] != 0:
                            flag = False
                            break
                    if flag:
                        bisect.insort(window, nums[right])
                        if len(window) > max_ans_len:
                            ans = nums[left:right+1]
                            max_ans_len = len(window)
                    else:
                        left = right
                        window.clear()
            right += 1
        return ans


    def largestDivisibleSubset2(self, nums: List[int]) -> List[int]:
        # 通过这道题，我之前理解的题意有点问题，这里的整除子集并不一定是nums数组的连续子集。
        # 既然不是连续子集，那么我们是否可以把nums数组排序呢。
        n = len(nums)
        nums.sort()
        dp = [1] * n  # 我们注意理解dp数组的含义，dp[i]表示的是以nums[i]作为整除子集最大数的长度。
        # 这道题搞了很久，dp初始化应该为1。
        ans = [[num] for num in nums]
        dp[0] = 1
        idx = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1
                    ans[i] = ans[j] + [nums[i]]
                    if dp[i] > dp[idx]:
                        idx = i
                    # 上面的if判断可以直接点。
                    # if len(ans[i]) > len(max_len):
                    #     max_len = ans[i]
        return ans[idx]


if __name__ == '__main__':
    solu = Solution()
    nums = [2, 3, 8, 9, 27]
    ans = solu.largestDivisibleSubset2(nums)
    print(ans)









