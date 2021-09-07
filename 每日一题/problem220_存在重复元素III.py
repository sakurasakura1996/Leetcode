import bisect
from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 暴力法试试看, 暴力法思路简单，但是超时了，时间复杂度是 O(nk) n,k的范围都是10^4级别，肯定会超时的啊
        n = len(nums)
        if n < 2:
            return False
        for i in range(n-1):
            for j in range(i+1, i+k+1):
                if j < n and abs(nums[i] - nums[j]) <= t:
                    return True
        return False

    def containsNearbyAlmostDuplicate2(self, nums: List[int], k: int, t: int) -> bool:
        # 暴力不行，我又有一个想法就是，把nums数组改造一下，按照大小排序，但是元素是 （值，索引），可以吗？
        # 如果，当前元素和下一个元素插值绝对值已经大于t了，那就不用找了，或者和下一个元素差值绝对值小于等于t，但是索引差值绝对值
        # 大于k的话，后续也不用找了，直接跳到下一个元素就行。这样的话，好像挺省时间的吧，try it
        n = len(nums)
        if n < 2:
            return False
        ans = []

        for i, num in enumerate(nums):
            ans.append([num, i])
        ans.sort(key=lambda x: (x[0], x[1]))
        # print(ans)
        for i in range(n-1):
            pre = ans[i]
            for j in range(i+1, n):
                nxt = ans[j]
                if abs(pre[0]-nxt[0]) > t:
                    break
                elif abs(pre[1] - nxt[1]) > k:
                    continue
                else:
                    return True
        return False

    def containsNearbyAlmostDuplicate3(self, nums: List[int], k: int, t: int) -> bool:
        # 题目归纳：数组中是否存在一个大小不超过t的子数组，其中的最大值和最小值差不超过k
        # 这道题目是固定长度求差值，1438题是固定差值求长度。任然使用滑动窗口方法，让滑动窗口固定大小为t
        # 本题最大难点为快速地找到滑动窗口中的最大最小值，以及删除指定元素，类似题目如 480
        # 如果遍历滑动窗口找到最大最小值，O(k)复杂度会超时，那么解决办法就是增加空间复杂度，找到合适的数据结构来做
        # 找一个内部有序的数据结构，C++中有set、multiset、map，java中有TreeSet，TreeMap，python中有SortedSet
        from sortedcontainers import SortedSet
        st = SortedSet()
        left, right = 0, 0
        ans = 0
        while right < len(nums):
            if right - left > k:
                st.remove(nums[left])
                left += 1
            index = bisect.bisect_left(st, nums[right]-t)
            if st and index >= 0 and index < len(st) and abs(st[index]-nums[right]) <= t:
                return True
            st.add(nums[right])
            right += 1
        return False


if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,3,1]
    k = 3
    t = 0
    ans = solu.containsNearbyAlmostDuplicate3(nums, k, t)
    print(ans)
