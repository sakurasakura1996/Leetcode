"""
自己再尝试写一下这道题，我们先不管什么小时分钟
"""
# 这个方法算是debug出来了，还是不够熟。还是题解中的code写的精炼。
from typing import List
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans = set()
        all = [i for i in range(10)]
        # hour_seen = set()
        # minute_seen = set()

        def backtrack(nums1: List[int], nums2: List[int], all: List[int], pos: int, hour: int, minute: int):
            # nums1为已选择的列表，nums2为可选择的列表,不好，nums2最好数据不动，那么他就是所有数据的列表
            # 还是不好说，看来题解中的代码还是写的挺好的，因为这是组合，不是排列，如果nums2数据不动的话，那么就是排列了。
            if hour > 11 or minute > 59:
                return
            if len(nums1)+len(nums2) == num:
                ans.add(f'{hour}:{minute:02}')
                return

            # 开始枚举
            for i in range(pos, len(all)):
                if all[i] < 4 and all[i] not in nums1:
                    nums1.append(all[i])
                    backtrack(nums1, nums2, all, pos+1, hour+int(pow(2, i)), minute)
                    nums1.remove(all[i])
                if all[i] >= 4 and all[i] not in nums2:
                    nums2.append(all[i])
                    backtrack(nums1, nums2, all, pos+1, hour, minute+int(pow(2, i-4)))
                    nums2.remove(all[i])
        backtrack([],[],all, 0, 0, 0)
        return ans

if __name__ == '__main__':
    solu = Solution()
    ans = solu.readBinaryWatch(2)
    print(ans)
    print(len(ans))