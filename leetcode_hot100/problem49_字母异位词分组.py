"""
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
"""
# 我们要注意，dict或者defaultdict这类字典，key值有限制的，不能使用动态变化的元素作为key。字符串是可以的，list列表是不可以的哦
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        ans = []
        # 字典的key不能是list吧。。。。。
        dict = defaultdict(list)
        for str in strs:
            tmp = list(str)
            tmp.sort()
            s = ''.join(tmp)
            dict[s].append(str)
        # 下面的写法不如写成
        # ans = list(dict.values())
        for key, value in dict.items():
            ans.append(value)
        return ans

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 计数的方法：由于互为字母异位词的两个字符串包含的字母相同，
        # 因此两个字符串中的相同字母出现的次数一定是相同的，故可以将每个字母出现的次数使用字符串表示，作为哈希表的键。
        # 需要注意的是，在使用数组作为哈希表的键时，不同语言的支持程度不同，因此不同语言的实现方式也不同。
        dict = defaultdict(list)

        for str in strs:
            counts = [0] * 26
            for ch in str:
                counts[ord(ch) - ord('a')] += 1
            # 需要将list转换成tuple才能进行哈希啊，这个点上次字节面试就遇到了，list不能作为hash的key，他是可变的。
            dict[tuple(counts)].append(str)
        return list(dict.values())



if __name__ == '__main__':
    solu = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans = solu.groupAnagrams(strs)
    print(ans)



