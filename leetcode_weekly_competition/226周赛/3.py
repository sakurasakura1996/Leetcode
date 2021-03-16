from typing import List
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(candiesCount)
        for i in range(1, n):
            candiesCount[i] += candiesCount[i-1]
        m = len(queries)
        ans = [True] * (m)
        for i in range(m):
            type, day, cap = queries[i][0], queries[i][1], queries[i][2]
            # 如果type==0的话，下面的type-1就会出现错误。所以别人的代码为什么可以写的这么简洁而且有效阿
            if cap * (day + 1) <= candiesCount[type-1]:
                ans[i] = False
                continue
            if day >= candiesCount[type]:
                ans[i] = False
                continue
        return ans

    # 别人的思路怎么就写的这么清晰呢，我当时是在想如何才能为True，大佬的解法是哪些情况为False。
    def canEat2(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        pre_sum = [0]
        for t in candiesCount:
            pre_sum.append(pre_sum[-1] + t)

        to_ret = []
        for favoriteTypei, favoriteDayi, dailyCapi in queries:
            to_add = True
            if dailyCapi * (favoriteDayi + 1) <= pre_sum[favoriteTypei]:
                to_add = False
            if favoriteDayi >= pre_sum[favoriteTypei + 1]:
                to_add = False
            to_ret.append(to_add)
        return to_ret


if __name__ == '__main__':
    solu = Solution()
    candiesCount = [7,4,5,3,8]
    queries = [[0,2,2], [4,2,4], [2,13,1000000000]]
    ans = solu.canEat2(candiesCount, queries)
    print(ans)


