from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrace(cur, path, tar):
            if tar == 0:
                ans.append(cur.copy())
                return
            for i, num in enumerate(path):
                if num > tar:   # 这里的判断要求它是有序的，因为num后面的数都要比前面大，那后面的数肯定都大于tar，那就不用考虑了
                    break
                cur.append(num)
                backtrace(cur, path[i:], tar-num)
                cur.pop()
        candidates.sort()
        backtrace([], candidates, target)
        return ans


if __name__ == '__main__':
    solu = Solution()
    candidates = [2,7,6,3,5,1]
    target = 9
    ans = solu.combinationSum(candidates, target)
    print(ans)
