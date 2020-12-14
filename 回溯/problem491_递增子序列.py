"""
491. 递增子序列
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
示例:
输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:
给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
"""
# 如果一个序列是递增的（包括相等），那么它的所有子序列除了空和只有一个元素，其他的应该都满足要求，那么我们可以把一个nums序列拆分啊
# 拆分成多个递增序列，如果整个nums数组是递增的，那就是一个序列。
# 之前刚看了回溯法，结果这里写不出来。哎，心累了
from typing import List
from collections import defaultdict

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # 回溯法 or DFS
        ans = []

        def backtrack(nums, track):
            if len(track) >=2 and track not in ans:
                ans.append(track)
            if not nums:
                return

            for i in range(len(nums)):
                # 判断track最后一个 是否小于 数组中的想要进来的数
                # 就是track是一个递增数组 进来的数必须大于track数组最后一个属
                if not track or nums[i] >= track[-1]:
                    backtrack(nums[i+1:], track+[nums[i]])

        backtrack(nums, [])
        return ans

    def findSubsequences_2(self, nums: List[int]) -> List[List[int]]:
        # BFS
        from collections import deque
        ans = []
        queue = deque([(nums, [])])
        while queue:
            cur, track = queue.popleft()
            if len(track) >= 2 and track not in ans:
                ans.append(track)
            for idx, i in enumerate(cur):
                if not track or i >= track[-1]:
                    queue.append(cur[idx+1:], track + [i])
        return ans

    """
    值得注意的是，上面两种解法中，将track加入到ans结果中时的判断都是 如果 track不在ans中，这个是比较耗时的。如果改用hash结构来避免
    重复，会更加高效一些。
    """
    def findSubsequences_2(self, nums: List[int]) -> List[List[int]]:
        # BFS
        from collections import deque
        ans = []
        queue = deque([(nums, [])])
        while queue:
            cur, track = queue.popleft()
            if len(track) >= 2:
                ans.append(track)
            curPres = defaultdict(int)
            # 思考一下，为什么用这个哈希字典可以解决重复问题，比如现在的cur是 [3,3,4]，当访问第一个3时，标价下来以访问，如果遍历第二个的3
            # 的时候不加以判断，结果会造成重复，因为第一个3会产生 [3,3,4](当然这个子序列并不会重复),[3,4]（这个就会和第2个3产生的子序列重复
            # 大概意思就是后面出现重复的值，直接舍去它所产生的子序列多没问题，因为前面的重复值肯定可以产生后面重复值所能产生的所有子序列
            # 也就是 [3,3,4]，由第一个3开头产生的子序列绝对是包括了第二个3产生的子序列。所以第二个3作为开头所产生的子序列可以直接过滤掉。
            # 这个地方看似简单，想明白并且以后很容易注意到还是挺难的，当然如果想简单的话还是上面代码中 track not in ans比较粗暴易理解
            for idx, i in enumerate(cur):
                if curPres[i]:
                    continue
                if not track or i >= track[-1]:
                    curPres[i] = 1
                    queue.append(cur[idx+1:], track + [i])
        return ans





