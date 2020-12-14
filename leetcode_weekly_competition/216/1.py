from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_str = ''.join(word1)
        word2_str = ''.join(word2)
        return word1_str == word2_str


solu = Solution()
word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
ans = solu.arrayStringsAreEqual(word1, word2)
print(ans)