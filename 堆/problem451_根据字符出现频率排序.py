"""
451. 根据字符出现频率排序
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:
输入:
"tree"
输出:
"eert"
解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

示例 2:
输入:
"cccaaa"
输出:
"cccaaa"
解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。

示例 3:
输入:
"Aabb"
输出:
"bbAa"
解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
"""
from collections import Counter
from heapq import *


class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        s_counter = Counter(s)
        sorted(s_counter.items(), key=lambda x: x[1], reverse=True)
        print(s_counter)
        # 这里感觉很怪异，我对计数器按照 value进行排序，print打印输出时还是对的，但是在遍历时，又改回了原来的顺序
        for key in s_counter.keys():
            tmp = key * s_counter[key]
            print(tmp)
            ans = ans + tmp
        return ans

    def frequencySort_2(self, s:str) -> str:
        ans = ""
        s_counter = Counter(s)
        # 改用Counter自带的排序功能了，most_common()不加参数表示对整体进行排序，返回一个列表
        s_list = s_counter.most_common()
        for key, value in s_list:
            ans += key * value
        return ans

    def frequencySort_3(self, s: str) -> str:
        # 做到这题是知道可以用堆来写的，所以这里写一下堆的解法,我们可以维护一个大顶堆，堆顶是 出现次数最多的节点
        heap = []
        s_counter = Counter(s)
        for key, value in s_counter.items():
            heappush(heap, (-value, key))   # 需要把value放在前面拥有堆的排序
        ans = ""
        while heap:
            value, key = heappop(heap)
            # print(key, value)
            ans += key * (-value)
        return ans


solu = Solution()
s = "Aabb"
ans = solu.frequencySort_3(s)
print(ans)
