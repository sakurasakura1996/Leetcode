from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # 使用前缀和的思想，保存所有的前缀异或结果
        n = len(queries)
        ans = []
        preXOR = [0]
        for a in arr:
            preXOR.append(preXOR[-1] ^ a)
        # print(preXOR)
        for l, r in queries:
            ans.append(preXOR[r+1] ^ preXOR[l])
        return ans

if __name__ == '__main__':
    solu = Solution()
    arr = [4,8,2,10]
    queries = [[2,3],[1,3],[0,0],[0,3]]
    ans = solu.xorQueries(arr, queries)
    print(ans)
