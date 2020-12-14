"""
描述
有一个商品列表，该列表是由L1、L2两个子列表拼接而成。当用户浏览并翻页时，需要从列表L1、L2中获取商品进行展示。
展示规则如下：
1. 用户可以进行多次翻页，用offset表示用户已经浏览过的商品数量。比如，offset是4，表示用户已经看了4个商品。
2. n表示一个页面可以展示的商品数量。
3. 展示商品时首先使用列表L1，如果列表L1不够，再从列表L2中选取商品。
4. 从列表L2中补全商品时，也可能存在数量不足的情况。
给定offset，n，列表L1和L2的长度。
请根据上述规则，计算列表L1和L2中哪些商品在当前页面被展示了。
你需要根据notice里的规则输出两个区间。区间段使用半闭半开区间表示，即包含起点，不包含终点。
比如，区间[0,1)表示第一个商品。如果某个列表的区间为空，使用[0, 0)表示，如果某个列表被跳过，使用[len, len)表示，len表示列表的长度。
示例
样例 1:
输入:
2
4
4
4
输出:
[2,4,0,2]

样例 2:
输入:
1
2
4
4
输出:
[1,3,0,0]
"""
# 理清思路比较重要，主要在于如何判断
class Solution:
    def ProductList(self, offset, n, len1, len2):
        if offset + n <= len1:
            # 全部都是L1中的商品
            return [offset,offset+n,0,0]
        elif offset <= len1:
            if n - len1 + offset > len2:
                return [offset, len1,0, len2]
            return [offset, len1,0,n-len1+offset]
        elif offset <= len1 + len2:
            if offset - len1 + n > len2:
                return [len1,len1,offset-len1,len2]
            return [len1,len1,offset-len1,offset-len1+n]
        else:
            return [len1,len1,len2,len2]

solu = Solution()
ans = solu.ProductList(1,2,4,4)
print(ans)



