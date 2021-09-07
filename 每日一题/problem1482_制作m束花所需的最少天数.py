from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        # 是否还是可以用二分法，然后只需要写 check 函数能验证是否能够满足要求
        left = min(bloomDay)
        right = max(bloomDay)

        def check(day):
            # 测试第day天是否能够制作出m束花来，必须要遍历一遍吗
            flower = 0
            cailiao = 0
            cur = 0
            while cur < n:
                if bloomDay[cur] <= day:
                    cailiao += 1
                    if cailiao == k:
                        flower += 1
                        cailiao = 0
                else:
                    cailiao = 0
                cur += 1
            return flower >= m

        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    solu = Solution()
    bloomDay = [1,10,2,9,3,8,4,7,5,6]
    m = 4
    k = 2
    ans = solu.minDays(bloomDay, m, k)
    print(ans)