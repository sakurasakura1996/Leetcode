from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        ans = [1] * (n+1)
        ans[0] = first
        for i in range(1, n+1):
            ans[i] = ans[i-1] ^ encoded[i-1]
        return ans


if __name__ == '__main__':
    solu = Solution()
    encoded = [6,2,7,3]
    first = 4
    ans = solu.decode(encoded, first)
    print(ans)



