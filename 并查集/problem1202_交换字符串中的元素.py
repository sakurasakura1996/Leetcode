"""
1202. 交换字符串中的元素
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
示例 1:
输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"

示例 2：
输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"

示例 3：
输入：s = "cba", pairs = [[0,1],[1,2]]
输出："abc"
解释：
交换 s[0] 和 s[1], s = "bca"
交换 s[1] 和 s[2], s = "bac"
交换 s[0] 和 s[1], s = "abc"
提示：
1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s 中只含有小写英文字母
"""
# date: 2021/1/11 好像昨天周赛也是这样一道题，思路很相近，应该用并查集来做，好好做一做这道题
# 这种题目，发现用并查集的思路倒不是很难，因为题目很容易发现是一个关系转换的过程，比如位置0的字符可以和位置1的字符交换
# 顺序，位置1的字符可以和位置2的字符交换顺序，那么位置0和位置2的字符也是可以交换顺序的，那么他们三个都是在同一个集合中。
# 然后只要在同一个集合中的字符，我们是可以实现任意顺序排列的，那么只要按照字典排序就行了。
# 然后还需要注意的是，可能最后归纳之后，还有好几个集合，这个时候我们要字典排序之后然后再放回到该集合所占的位置上去。
from typing import List
from collections import defaultdict
class F:
    def __init__(self, s: str, pairs: List[List[int]]):
        self.index = list(range(len(s)))
        for left, right in pairs:
            if left > right:
                left, right = right, left
            self.union(left, right)

    def find(self, x):
        while x != self.index[x]:
            x = self.index[x]
        return x

    def union(self, p, q):
        # 两个集合原来是独立的，这个时候它们产生了联系，那么就可以完全联系起来了。
        p_parent = self.find(p)
        q_parent = self.find(q)
        if p_parent != q_parent:

            for i, item in enumerate(self.index):
                if item == q_parent:
                    self.index[i] = p_parent

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 对并查集的使用还是搞不太懂，知道有数组就可以了，但是用数组怎么来赋予涵义
        s_list = list(s)
        print(s_list)
        f = F(s, pairs)
        s_defaultdict = defaultdict(list)
        for i, item in enumerate(f.index):
            s_defaultdict[item].append(i)
        for key, value in s_defaultdict.items():
            tmp = ""
            for item in value:
                tmp += s[item]
            tmp = sorted(tmp)
            for i, ch in enumerate(tmp):
                s_list[value[i]] = ch
        return "".join(s_list)


if __name__ == '__main__':
    solu = Solution()
    s = "cba"
    pairs = [[0,1],[1,2]]
    ans = solu.smallestStringWithSwaps(s, pairs)
    print(ans)

# 上面的写法应该是没有问题的了，但是还是超出时间限制了。

