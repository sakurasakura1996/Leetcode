from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counter = Counter(words)
        # 出现次数相同的时候，再按照字母顺序来排序。可以将某一个参数取反，统一起来
        ans = sorted(word_counter.items(), key=lambda x:(-x[1],x[0]))
        ret = []
        for i in range(k):
            ret.append(ans[i][0])
        return ret


if __name__ == '__main__':
    solu = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    ans = solu.topKFrequent(words, k)
    print(ans)
