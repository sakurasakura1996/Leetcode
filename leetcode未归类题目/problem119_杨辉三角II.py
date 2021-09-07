from typing import List
class Solution:
    def getRow(self, numRows: int) -> List[int]:
        if numRows == 0:
            return [1]
        elif numRows == 1:
            return [1, 1]
        else:
            cur = [1, 1]
            num = 1
            while num < numRows:
                for i in range(len(cur)-1, 0, -1):
                    cur[i] = cur[i] + cur[i-1]
                cur.append(1)
                num += 1
            return cur

if __name__ == '__main__':
    solu = Solution()
    ans = solu.getRow(4)
    print(ans)
