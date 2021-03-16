from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 暴力法的话，大概率是会超时的
        n = len(T)
        ans = [0] * n
        for i in range(n-1):
            for j in range(i+1, n):
                if T[i] < T[j]:
                    ans[i] = j - i
                    break
        return ans

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 我们想想为什么上面的过程会超时呢，因为我们在固定一个点时，每次都是独立的去往后遍历，这样会重复很多次。
        # 怎么解决呢
        n = len(n)
        ans, nxt, big = [0] * n, dict(), float('inf')
        for i in range(n-1, -1, -1):
            warmer_idx =


if __name__ == '__main__':
    solu = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    ans = solu.dailyTemperatures(temperatures)
    print(ans)


