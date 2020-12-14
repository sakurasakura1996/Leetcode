"""
1550. 存在连续三个奇数的数组
给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 true ；否则，返回 false 。
示例 1：
输入：arr = [2,6,4,1]
输出：false
解释：不存在连续三个元素都是奇数的情况。
示例 2：
输入：arr = [1,2,34,3,4,5,7,23,12]
输出：true
解释：存在连续三个元素都是奇数的情况，即 [5,7,23] 。
提示：
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""
# 滑动窗口即可
from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if not arr or len(arr) < 3:
            return False
        n = len(arr)
        left = 0
        right = 0
        num = 0  # 用于记录窗口中有几个连续的奇数
        while right < n:
            if arr[right] % 2 == 1:
                right += 1
                num += 1
                if num == 3:
                    return True
            else:
                right += 1
                num = 0
        return False


solu = Solution()
arr = [2, 6, 4, 1]
ans = solu.threeConsecutiveOdds(arr)
print(ans)
