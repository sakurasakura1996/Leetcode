from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        strs_dict = defaultdict(list)
        if not strs:
            return ans
        for str in strs:
            temp = ''.join(sorted(list(str)))
            strs_dict[temp].append(str)
        ans = list(strs_dict.values())
        return ans

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # 我们可以用每个字符串中各种字母出现的次数作为hash表的key值
        strs_dict = defaultdict(list)

        for str in strs:
            counts = [0] * 26
            for ch in str:
                counts[ord(ch)-ord('a')] += 1
            # 需要将list转成tuple元组才能作为hash表的key
            strs_dict[tuple(counts)].append(str)
        return list(strs_dict.values())




if __name__ == '__main__':
    solu = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans = solu.groupAnagrams(strs)
    print(ans)