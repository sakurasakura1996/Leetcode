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
# 对于下面的回溯算法代码，我感觉还挺难写的，我理解成下面的解释：
# 因为有十个灯，然后有num个灯亮，我们先不要管什么hour和minute，那么问题就变成了比较好容易理解一点的回溯
#
from typing import List
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        hour_seen = set()
        minute_seen = set()

        def backtrace(num: int, hour: int, minute: int, which: int)->None:
            if hour > 11 or minute > 59:
                return
            if num == 0:
                res.append(f'{hour}:{minute:02}')  # 这里的02是 0width的意思，width指定宽度，开头的0指定高位用0补足宽度
                return
            # 枚举hour可能，对应h是2^h
            for h in range(which, 4):
                if h not in hour_seen:
                    hour_seen.add(h)
                    backtrace(num-1, hour+int(pow(2, h)), minute, h+1)
                    hour_seen.remove(h)

            # 枚举minute可能，对应m是2^(m-4)
            for m in range(max(which, 4), 10):
                if m not in minute_seen:
                    minute_seen.add(m)
                    backtrace(num-1, hour, minute+int(pow(2, m-4)), m+1)
                    minute_seen.remove(m)
        backtrace(num, 0, 0, 0)
        return res


if __name__ == '__main__':
    solu = Solution()
    ans = solu.readBinaryWatch(2)
    print(ans)
    print(len(ans))


