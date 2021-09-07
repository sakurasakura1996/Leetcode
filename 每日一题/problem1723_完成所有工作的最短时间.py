from typing import List
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        left = max(jobs)
        right = sum(jobs)

        def check(limit):
            # check下 limit的时候能否分配给k个工人完成工作。
            arr = sorted(jobs)
            groups = [0] * k
            if backtrace(arr, groups, limit):
                return True
            else:
                return False

        def backtrace(arr, groups, limit):
            # 回溯尝试每种可能
            if not arr:
                return True
            v = arr.pop()

            for i in range(k):
                if groups[i] + v <= limit:
                    groups[i] += v
                    if backtrace(arr, groups, limit):
                        return True
                    groups[i] -= v

                    # 需要剪枝啊，不然不好通过
                    if groups[i] == 0:
                        break
            arr.append(v)
            return False

        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    solu = Solution()
    jobs = [1,2,4,7,8]
    k = 2
    ans = solu.minimumTimeRequired(jobs, k)
    print(ans)
