from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 没有思路的话，我感觉这道题目主要需要通过 DFS来做。
        if n == 0:
            return [0]
        ans = [0]
        for i in range(1, n+1):
            ans = [2 * k for k in ans] + [2 * k + 1 for  k in ans[::-1]]
        return ans

if __name__ == '__main__':
    solu = Solution()
    ans = solu.grayCode(2)
    print(ans)
        