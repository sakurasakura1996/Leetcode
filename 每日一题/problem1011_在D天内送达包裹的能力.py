from typing import List
class Solution:
    # 首先理解下题目意思，题目角度：可以理解成让你找到一条最小载重的船，但是能保证D天运输完成。
    # 我其实是想用二分法来试试
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n = len(weights)
        weight_sum = sum(weights)
        left = max(weights)   # 错误的原因主要在这里，直接取平均并不是左边界。
        right = weight_sum

        def check(mid):
            days = 1
            s = 0
            for weight in weights:
                if s + weight <= mid:
                    # days不变，s += weight
                    s += weight
                elif s + weight > mid:
                    s = weight
                    days += 1
            if days > D:
                return False
            else:
                return True
        # print(check(6))
        while left < right:
            mid = left + (right - left) // 2
            # 测试 mid 值
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return right

    # made，上面的二分法搞了大半天还是通不过，我吐了。。。
    def shipWithinDays2(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            days = 1
            weigth_sum = 0
            for weight in weights:
                if weigth_sum + weight > mid:
                    days += 1
                    weigth_sum = 0
                weigth_sum += weight
            if days <= D:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solu = Solution()
    weights = [1,2,3,4,5,6,7,8,9,10]
    D = 5
    ans = solu.shipWithinDays(weights, D)
    print(ans)





