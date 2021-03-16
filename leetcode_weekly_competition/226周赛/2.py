
from typing import List
from collections import defaultdict, Counter
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pairs = defaultdict(list)
        m = len(adjacentPairs)
        ans = [0] * (m+1)
        for i in range(m):
            left, right = adjacentPairs[i][0], adjacentPairs[i][1]
            pairs[left].append(right)
            pairs[right].append(left)
        start = 0
        for key, value in pairs.items():
            if len(value) == 1:
                start = key
                break
        ans[0] = start
        for i in range(1, m+1):
            if len(pairs[start]) == 1:
                ans[i] = pairs[start][0]
            else:
                left, right = pairs[start][0], pairs[start][1]
                if ans[i-2] == left:
                    ans[i] = right
                else:
                    ans[i] = left
            start = ans[i]
        return ans

    # 下面是大佬的解法，其实思路是一样的，但是我上面的代码写的就冗余狗屎阿。。。
    def restoreArray2(self, adjacentPairs: List[List[int]]) -> List[int]:
        dictt = defaultdict(lambda: [])
        counter = Counter()
        for a, b in adjacentPairs:
            dictt[a].append(b)
            dictt[b].append(a)
            counter[a] += 1
            counter[b] += 1
        for start in counter:
            if counter[start] % 2 == 1:
                break
        to_ret = [-1, start]
        while len(to_ret) - 1 <= len(adjacentPairs):
            nextt = [t for t in dictt[to_ret[-1]] if not t == to_ret[-2]][0]
            to_ret.append(nextt)
        return to_ret[1:]


if __name__ == '__main__':
    solu = Solution()
    adjacentPairs = [[4,-2],[1,4],[-3,1]]
    ans = solu.restoreArray(adjacentPairs)
    print(ans)
