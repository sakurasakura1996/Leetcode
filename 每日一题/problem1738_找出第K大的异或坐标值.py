from typing import List
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        # 别问，首先暴力
        m = len(matrix)
        n = len(matrix[0])
        pre = [[0] * (n+1) for _ in range(m+1)]
        ans = []
        for i in range(1, m+1):
            for j in range(1, n+1):
                pre[i][j] = pre[i-1][j] ^ pre[i][j-1] ^ pre[i-1][j-1] ^ matrix[i-1][j-1]
                ans.append(pre[i][j])
        ans.sort(reverse=True)
        return ans[k-1]


if __name__ == '__main__':
    solu = Solution()
    matrix = [[5, 2], [1, 6]]
    k = 1
    ans = solu.kthLargestValue(matrix, k)
    print(ans)
