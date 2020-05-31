"""
239 滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。
进阶：
你能在线性时间复杂度内解决此题吗？
示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
提示：
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

此方法如果直接用暴力法的话会觉得完全不是困难程度的题目，下面先用了暴力法解决问题，遍历nums数组已经是O(N)了
但是，每个滑动窗口中的k个值还需要找出最大的，k个值中找出最大值的最好的时间复杂度是O(k)所以总的时间复杂度就是
O(Nk)了，而这题是要你实现 线性时间复杂度。
"""

## way1 暴力求解法
# from typing import List
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         left = 0
#         right = k
#         ans = []
#         while right <= len(nums):
#             window = nums[left:right]
#             cur_max = max(window)
#             ans.append(cur_max)
#             left += 1
#             right += 1
#         return ans

# way2 双向队列方法
# from typing import List
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         ans = []
#         right = 0
#         window = []
#         while right < len(nums):
#             if len(window)!=0 and window[0] <= right - k:
#                 window.pop(0)
#             while len(window)!=0 and nums[right] > nums[window[-1]]:
#                 window.pop(-1)
#             window.append(right)
#             right += 1
#             if right >= k:
#                 ans.append(nums[window[0]])
#         return ans


# way3 动态规划方法，官网给的题解，看了半天没有理解到其中的精髓，感觉下次做同种题目还是想不到啊
# 最后看到一个符合动态规划思想的思路和代码，但是自己感觉时间复杂度并不是线性的。
# dp[i] 表示窗口左侧在原数组索引i所在位置时吗，对应最大值所在的索引.这个方法相比官网给的动态规划理解要习惯很多。官网的说法感觉
# 更像是双向遍历的感觉。 后面两种发现，都是存索引，而不是存窗口的值。因为这样的话既可以知道窗口中的值，还可以对他们进行排序。
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        dp = [0 for i in range(len(nums)-k+1)]
        res = [0 for i in range(len(nums)-k+1)]
        for i in range(1, k):
            if nums[i] >= nums[dp[0]]:
                dp[0] = i
        res[0] = nums[dp[0]]
        # print(res[0])
        for j in range(1, len(dp)):
            if nums[j+k-1] >= nums[dp[j-1]]:
                dp[j] = j+k-1
            else:
                if dp[j-1] == j-1:
                    # 上一个窗口的最大值在最左侧时
                    dp[j] = j
                    for q in range(j+1, k+j):
                        if nums[q] >= nums[dp[j]]:
                            dp[j] = q
                else:
                    dp[j] = dp[j-1]
            res[j] = nums[dp[j]]
        return res




solu = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
ans = solu.maxSlidingWindow(nums,k)
print(ans)