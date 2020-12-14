"""
401. 二进制手表
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。
每个 LED 代表一个 0 或 1，最低位在右侧。

例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

示例：
输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
提示：
输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
超过表示范围（小时 0-11，分钟 0-59）的数据将会被舍弃，也就是说不会出现 "13:00", "0:61" 等时间。
"""
# 我们可以先不着急想到底是hour还是minute，就是1到10八个灯。
from typing import List
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        ans = set()
        all = [i for i in range(10)]

        def backtrace(nums1: List[int], nums2: List[int], all: List[int], pos: int, hour: int, minute: hour):
            if hour > 11 or minute > 59:
                return
            if len(nums1) + len(nums2) == num:
                ans.add(f'{hour}:{minute:02}')
                return

            # 开始枚举l
            for i in range(pos, len(all)):
                if all[i] < 4 and all[i] not in nums1:
                    nums1.append(all[i])
                    backtrace(nums1, nums2, all, pos+1, hour+int(pow(2, i)), minute)
                    nums1.remove(all[i])

                if all[i] >= 4 and all[i] not in nums2:
                    nums2.append(all[i])
                    backtrace(nums1, nums2, all, pos+1, hour, minute+int(pow(2, i-4)))
                    nums2.remove(all[i])
        backtrace([], [], all, 0, 0, 0)
        return ans

    def readBinaryWatch2(self, num:int) -> List[str]:

        hour_seen = set()
        minute_seen = set()
        ans = set()

        def backtrace(length:int, hour: int, minute: int, pos: int):
            if hour > 11 or minute > 59:
                return
            if length == num:
                ans.add(f'{hour}:{minute:02}')

            for i in range(pos, 10):
                if i < 4 and i not in hour_seen:
                    hour_seen.add(i)
                    backtrace(length+1, hour+int(pow(2, i)), minute, i+1)
                    hour_seen.remove(i)

                if i >= 4 and i not in minute_seen:
                    minute_seen.add(i)
                    backtrace(length+1, hour, minute+int(pow(2, i-4)), i+1)
                    minute_seen.remove(i)
        backtrace(0, 0, 0, 0)
        ans = list(ans)
        ans.sort()
        return ans


if __name__ == '__main__':
    solu = Solution()
    ans = solu.readBinaryWatch2(2)
    print(ans)

