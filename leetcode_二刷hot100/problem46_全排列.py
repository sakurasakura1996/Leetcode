from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrace(cur, path):
            # cur为已选，path为待选
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            for i, num in enumerate(path):
                cur.append(num)
                tmp = path[:i]+path[i+1:]
                backtrace(cur, tmp)
                cur.pop()

        backtrace([], nums)
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 3]
    ans = solu.permute(nums)
    print(ans)


