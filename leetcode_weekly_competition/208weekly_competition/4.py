"""
5526. 最多可达成的换楼请求数目
我们有 n 栋楼，编号从 0 到 n - 1 。每栋楼有若干员工。由于现在是换楼的季节，部分员工想要换一栋楼居住。
给你一个数组 requests ，其中 requests[i] = [fromi, toi] ，表示一个员工请求从编号为 fromi 的楼搬到编号为 toi 的楼。
一开始 所有楼都是满的，所以从请求列表中选出的若干个请求是可行的需要满足 每栋楼员工净变化为 0 。意思是每栋楼 离开 的员工数目 等于
该楼 搬入 的员工数数目。比方说 n = 3 且两个员工要离开楼 0 ，一个员工要离开楼 1 ，一个员工要离开楼 2 ，如果该请求列表可行，
应该要有两个员工搬入楼 0 ，一个员工搬入楼 1 ，一个员工搬入楼 2 。
请你从原请求列表中选出若干个请求，使得它们是一个可行的请求列表，并返回所有可行列表中最大请求数目。
示例 1：
输入：n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
输出：5
解释：请求列表如下：
从楼 0 离开的员工为 x 和 y ，且他们都想要搬到楼 1 。
从楼 1 离开的员工为 a 和 b ，且他们分别想要搬到楼 2 和 0 。
从楼 2 离开的员工为 z ，且他想要搬到楼 0 。
从楼 3 离开的员工为 c ，且他想要搬到楼 4 。
没有员工从楼 4 离开。
我们可以让 x 和 b 交换他们的楼，以满足他们的请求。
我们可以让 y，a 和 z 三人在三栋楼间交换位置，满足他们的要求。
所以最多可以满足 5 个请求。

示例 2：
输入：n = 3, requests = [[0,0],[1,2],[2,1]]
输出：3
解释：请求列表如下：
从楼 0 离开的员工为 x ，且他想要回到原来的楼 0 。
从楼 1 离开的员工为 y ，且他想要搬到楼 2 。
从楼 2 离开的员工为 z ，且他想要搬到楼 1 。
我们可以满足所有的请求。

示例 3：
输入：n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
输出：4
提示：
1 <= n <= 20
1 <= requests.length <= 16
requests[i].length == 2
0 <= fromi, toi < n
"""
# https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests/solution/python3-zu-he-jian-zhi-si-lu-xiang-jie-cong-bao-li/
from typing import List
class Solution:
    # 找到图中所有的环，计算环上的线条数。并不是所有环，如果有两个环相交，找最大环。其实这个想法应该不太能实现啊。
    # 题解作者看到这题，由于数据量不大，所以试了一下枚举。
    # 尼玛这个枚举的代码我看了好久。哭了啊。
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def check(code):
            cur = [0] * n
            count = 0
            for i, (L, R) in enumerate(requests):
                if (1 << i) & code:
                    count += 1
                    cur[L] += 1
                    cur[R] -= 1
            return 0 if any(cur) else count
        return max(map(check, range(1 << len(requests))))


# 对于枚举来说，缩小样本空间永远是最有效的做法。就本题而言，具体来说分三步：
# 1.对于request[i] = [j, j]，指向源节点的请求，直接选中
# 2.如果某个节点的入度为0或者出度为0，那么和该节点相关的请求全部放弃：
# 3.不断重复（2),剔除掉端点的入度或出度为0的请求。

from collections import defaultdict, Counter
import itertools
class Solution2:
    def maximumRequests(self, n:int, requests: List[List[int]]):
        # 排除指向自身的边
        go_back_home = sum(1 for L, R in requests if L == R)

        # 按入度和出度剪枝
        In, Out = defaultdict(Counter), defaultdict(Counter)
        for L, R in requests:
            if L != R:
                Out[L][R]+=1
                In[R][L] += 1

        # 剔除入度或者出度为0的节点以及请求。
        remove = [i for i in range(n) if not In[i] or not Out[i]]

        for i in remove:
            for L in In[i]:
                Out[L][i] -= 1
                if not Out[L][i]:Out[L].pop(i)
                if not Out[L]: remove.append(L)
            for R in Out[i]:
                In[R][i]-=1
                if not In[R][i]:In[R].pop(i)
                if not In[R]: remove.append(R)
            In.pop(i)
            Out.pop(i)
        requests = sum(([(L,R)]*Out[L][R] for L in Out for R in Out[L]),[])

        # 组合
        for k in range(len(requests), 0, -1):
            for c in itertools.combinations(requests, k):
                degree = [0] * n
                for L, R in c:
                    degree[L] -= 1
                    degree[R] += 1
                if not any(degree):
                    return k + go_back_home
        return go_back_home

# 立即推，放弃此题。