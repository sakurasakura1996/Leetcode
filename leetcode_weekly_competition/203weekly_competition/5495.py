from typing import List
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        ans = []
        dic = [0] * (n+1)
        dic[rounds[0]] = 1
        m = len(rounds)
        for i in range(m-1):
            start = rounds[i]
            end = rounds[i+1]
            if start < end:
                for j in range(start+1, end+1):
                    dic[j] += 1
            else:
                for j in range(start+1, n+1):
                    dic[j] += 1
                for j in range(1,end+1):
                    dic[j] += 1

        maxnum = max(dic)
        for i in range(1,n+1):
            if dic[i] == maxnum:
                ans.append(i)
        return ans

solu = Solution()
n = 7
rounds = [1,3,5,7]
ans = solu.mostVisited(n, rounds)
print(ans)


