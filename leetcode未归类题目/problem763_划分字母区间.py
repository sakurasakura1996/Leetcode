""""
763. 划分字母区间
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
示例 1：
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
提示：
S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。
"""
# 我的思路就是先统计每个字符的起始位置和终止位置，然后不断遍历可能的位置组合。
from typing import List
from collections import defaultdict
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n = len(S)
        dic = defaultdict(list)
        for i in range(n):
            ch = S[i]
            if dic[ch]:
                dic[ch][1] = i
            else:
                dic[ch] = [i, i]

        ans = []
        left = right = 0
        while right < n:
            flag = True
            for key, value in dic.items():
                start, end = value
                if (start >= left and end <= right) or (start > right) or (end < left):
                    continue
                else:
                    flag = False
                    break
            if flag:
                ans.append(right - left + 1)
                left = right+1
                right += 1
            else:
                right += 1
        return ans
    # 看完题解发现题解中的思路更加清晰简单一些
    def partitionLabels2(self, S: str) -> List[int]:
        last = [0] * 26  # 只需要记录每个字符最终出现的位置就行了
        for i, ch in enumerate(S):
            last[ord(ch) - ord('a')] = i

        partition = list()
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord('a')])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
        return partition


solu = Solution()
S = "ababcbacadefegdehijhklij"
ans = solu.partitionLabels2(S)
print(ans)



