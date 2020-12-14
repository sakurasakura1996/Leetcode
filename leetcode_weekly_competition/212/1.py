from typing import List
from collections import defaultdict
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        dic = defaultdict(int)
        for i, s in enumerate(keysPressed):
            if i == 0:
                dic[s] = releaseTimes[0]
            else:
                time = releaseTimes[i] - releaseTimes[i-1]
                if dic[s]:
                    if time > dic[s]:
                        dic[s] = time
                else:
                    dic[s] = time
        key_list = sorted(dic)
        ans = key_list[0]
        res = dic[ans[0]]
        for a in key_list:
            if dic[a] >= res:
                ans = a
                res = dic[a]
        return ans

solu = Solution()
releaseTimes = [12,23,36,46,62]
keysPressed = "spuda"
ans = solu.slowestKey(releaseTimes, keysPressed)
print(ans)