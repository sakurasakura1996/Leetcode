from typing import List
import sys
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        n = len(logs)
        ans = 0
        for log in logs:
            if log == "./":
               continue
            elif log == "../":
                ans = max(ans-1, 0)
            else:
                ans += 1
        return ans


solu = Solution()
logs = ["d1/","../","../","../"]
ans = solu.minOperations(logs)
print(ans)


