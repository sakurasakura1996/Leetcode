from typing import List
from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # 感觉这个方法还挺好的了，但是竟然还是超时，主要是因为，wall的长度和宽度都是10^4级别，这样还是太高了。
        m = len(wall)
        n = sum(wall[0])
        ans = defaultdict()
        ret = 0
        for wa in wall:
            start = 0
            for i in range(0, len(wa)-1):
                start += wa[i]
                if start not in ans.keys():
                    ans[start] = 1
                else:
                    ans[start] += 1
                ret = max(ret, ans[start])

        return m - ret


if __name__ == '__main__':
    solu = Solution()
    wall = [[1],[1],[1]]
    ans = solu.leastBricks(wall)
    print(ans)


