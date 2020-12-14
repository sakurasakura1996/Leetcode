"""
239. 滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
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
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""
# 在已知可以用单调栈的基础上来做的这道题目，但是其中有一个问题就是，如果滑动窗口导致最大值出去了怎么办
# 我还是没有了解透彻，这里可以使用递减栈，如果栈的长度大于窗口的长度时，就让栈底元素出栈，这种操作可以解决上面提到的问题。
# 递减栈，栈底是最大元素，同时它上面的元素一定更比它靠后啊，所以栈的长度大于窗口长度时，这个最大值是肯定要滚蛋了，
# 如果新来了一个比最大元素更大的数也没关系，栈中所有元素全部要出栈，然后栈中就只有这一个最大元素，这也没关系啊，栈的长度现在为1，
# 可以每移动一次窗口就返回一次栈底元素啦。

# 上面说了这么多，其实这道题只用了递减栈的思想，题解中说的解法应该都算是双端队列问题。

from typing import List
import heapq
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 递减栈还是没有搞出来，。。我们需要存储索引位置宝贝，还是可以的
        n = len(nums)
        stack = list()
        ans = []
        for i in range(n):
            if stack and stack[0] <= i - k:
                stack.pop(0)
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
            ans.append(nums[stack[0]])
        return ans[k-1:]

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        # 堆的方法，我们创建一个大顶堆，维持堆的元素个数为k个。heapq自带的堆模块实现的是最大堆。数值型的话可以直接取反转换为最小堆。
        heap = []
        n = len(nums)
        ans = []
        for i in range(n):
            # 我们要记录下每个元素在原来数组的位置，这个很重要。
            heapq.heappush(heap, (-nums[i], i))
            if i + 1 >= k:
                while heap and heap[0][1] < i + 1 - k:
                    heapq.heappop(heap)
                ans.append(-heap[0][0])
        return ans

    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

    def maxSlidingWindow4(self, nums: List[int], k: int) -> List[int]:
        ans = []
        right = 0
        window = []
        while right < len(nums):
            if len(window) != 0 and window[0] <= right - k:
                window.pop(0)
            while len(window) != 0 and nums[right] > nums[window[-1]]:
                window.pop(-1)
            window.append(right)
            right += 1
            if right >= k:
                ans.append(nums[window[0]])
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    ans = solu.maxSlidingWindow(nums, k)
    print(ans)

