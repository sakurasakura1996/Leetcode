from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        n = len(accounts)
        for i in range(n):
            ans = max(ans, sum(accounts[i]))
        return ans

solu = Solution()
accounts = [[2,8,7],[7,1,3],[1,9,5]]
ans = solu.maximumWealth(accounts)
print(ans)