from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for en in encoded:
            tmp = first ^ en
            ans.append(tmp)
            first = tmp
        return ans

if __name__ == '__main__':
    solu = Solution()
    encoded = [6, 2, 7, 3]
    first = 4
    ans = solu.decode(encoded, first)
    print(ans)