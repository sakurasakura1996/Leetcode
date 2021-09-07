from typing import List
from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 还是滑动窗口方法来写,因为向有序集合中添加删除元素，时间复杂度是O(logn)级别，所以整体算法时间复杂度是O(nlogn)级别
        n = len(nums)
        left = right = 0
        window = SortedList()
        # 记住这里SortedSet不存储重复元素的，所以应该用left和right来计算数组长度。
        ans = 0
        while right < n:
            window.add(nums[right])
            right += 1
            while window and abs(window[-1] - window[0]) > limit:
                # 这里写的还是有问题啊，因为SortedSet相同元素只存储一次，如果我在这里执行删除的话，那么其余重复的元素就删不掉了啊
                window.remove(nums[left])
                left += 1
            if window and right - left > ans:
                ans = right - left
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [8,2,4,7]
    limit = 4
    ans = solu.longestSubarray(nums, limit)
    print(ans)
