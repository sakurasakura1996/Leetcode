from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows == 0:
            return ans
        ans = []
        for i in range(numRows):
            tmp = [1] * (i+1)
            if i > 1:
                for j in range(1, i):
                    tmp[j] = ans[i-1][j-1]+ans[i-1][j]
            ans.append(tmp.copy())
        return ans


if __name__ == '__main__':
    solu = Solution()
    ans = solu.generate(5)
    print(ans)
